"""
IPTV-4GTV Rebuild - Runnable Version
基於 Docker 映像反編譯資訊重建
"""
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
import os
import secrets

app = FastAPI(title="IPTV-4GTV", version="1.0.0")

# 設置模版目錄 - 在 Docker 中為 /app/templates
TEMPLATE_DIR = "/app/templates" if os.path.exists("/app/templates") else "app/templates"

def render_template(filename: str) -> HTMLResponse:
    """讀取靜態 HTML 模板"""
    path = os.path.join(TEMPLATE_DIR, filename)
    try:
        with open(path, "r", encoding="utf-8") as f:
            return HTMLResponse(f.read())
    except FileNotFoundError:
        return HTMLResponse(f"<h1>Template {filename} not found</h1>")

# ==================== 設定模型 ====================
class AdminInitData(BaseModel):
    admin_user: str
    admin_pwd: str

class UpdateTokenData(BaseModel):
    action: str
    custom_token: Optional[str] = None
    token_to_delete: Optional[str] = None

class UpdateProxyData(BaseModel):
    servers: Dict[str, List[Dict]]

# ==================== 全域變數 ====================
PROXY_HOST = os.getenv("PROXY_HOST", "0.0.0.0")
XRAY_PORT = int(os.getenv("XRAY_PORT", "1080"))
ADMIN_USER = os.getenv("ADMIN_USER", "")
ADMIN_PWD = os.getenv("ADMIN_PWD", "")

proxy_servers: Dict[str, List] = {"vless": [], "vmess": [], "trojan": []}
valid_tokens: List[str] = []
current_token: str = ""

# ==================== 路由端點 ====================

@app.get("/", response_class=HTMLResponse)
async def root_handler():
    """根路由 -> 重定向到登入"""
    return RedirectResponse(url="/login")

# ---------- 認證相關 ----------
@app.get("/login", response_class=HTMLResponse)
async def login_page():
    """登入頁面"""
    return render_template("admin_login.html")

@app.post("/login")
async def login(request: Request, admin_user: str = Form(), admin_pwd: str = Form()):
    """處理登入"""
    if admin_user == ADMIN_USER and admin_pwd == ADMIN_PWD:
        return RedirectResponse(url="/config/proxy", status_code=303)
    return HTMLResponse(render_template("admin_login.html").body + '<div class="alert alert-danger">帳號或密碼錯誤</div>')

@app.get("/logout")
async def logout():
    """登出"""
    return RedirectResponse(url="/login")

# ---------- 管理員初始化 ----------
@app.get("/admin/init")
async def admin_init_page():
    """管理員初始化頁面"""
    return render_template("admin_init.html")

# ---------- Token 管理 ----------
@app.get("/config/token")
async def token_config_page():
    """Token 設定頁面"""
    return render_template("token_config.html")

@app.post("/config/update-token")
async def update_token(data: UpdateTokenData):
    """更新 Token"""
    global current_token, valid_tokens
    
    response = {"success": True, "message": ""}
    
    if data.action == "generate":
        current_token = secrets.token_hex(32)
        valid_tokens = [current_token]
        response["message"] = "已生成新 Token"
    elif data.action == "add_custom" and data.custom_token:
        valid_tokens.append(data.custom_token)
        response["message"] = "已新增自定義 Token"
    
    return response

# ---------- 代理設定 ----------
@app.get("/config/proxy")
async def proxy_config_page():
    """代理設定頁面"""
    return render_template("proxy_config.html")

@app.get("/config/proxy-servers")
async def get_proxy_servers():
    """取得代理伺服器列表"""
    return {"success": True, "servers": proxy_servers}

@app.post("/config/update-proxy-servers")
async def update_proxy_servers(data: UpdateProxyData):
    """更新代理伺服器配置"""
    global proxy_servers
    proxy_servers = data.servers
    return {"success": True, "message": "代理伺服器已更新"}

@app.post("/config/test-{proxy_type}")
async def test_proxy_latency(proxy_type: str, server: Dict = None):
    """測試代理連線延遲 - 模擬結果"""
    return {"success": True, "latency": 50}

# ---------- 播放清單 ----------
@app.get("/get_m3u")
async def get_m3u():
    """取得 M3U 播放清單"""
    m3u_path = "/app/m3u.txt" if os.path.exists("/app/m3u.txt") else "app/m3u.txt"
    try:
        with open(m3u_path, "r") as f:
            content = f.read()
        return HTMLResponse(content, media_type="application/vnd.apple.mpegurl")
    except:
        return HTMLResponse("#EXTM3U\n")

@app.get("/get_txt")
async def get_txt():
    """取得 TXT 播放清單"""
    txt_path = "/app/txt.txt" if os.path.exists("/app/txt.txt") else "app/txt.txt"
    try:
        with open(txt_path, "r") as f:
            return f.read()
    except:
        return ""

# ---------- 系統狀態 ----------
@app.get("/status")
async def system_status_page():
    """系統狀態頁面"""
    return render_template("system_status.html")

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/ready")
async def readiness_check():
    return {"ready": True}

# ==================== 啟動/關閉 ====================

@app.on_event("startup")
async def startup_event():
    """應用程式啟動"""
    print("IPTV-4GTV 服務已啟動")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", "5050")))