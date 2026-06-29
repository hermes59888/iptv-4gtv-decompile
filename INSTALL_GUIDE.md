# Docker Desktop 安裝與反編譯指南

## 安裝 Docker Desktop

```bash
# 方法 1: 圖形介面安裝
open /tmp/docker.pkg

# 方法 2: 命令列安裝 (需要管理員密碼)
sudo installer -pkg /tmp/docker.pkg -target /

# 安裝完成後啟動 Docker
open -a Docker
```

## 完整反編譯指令

### 1. 載入 Docker 映像
```bash
docker pull instituteiptv/iptv-4gtv:latest
```

### 2. 提取映像層
```bash
docker save instituteiptv/iptv-4gtv:latest -o iptv-4gtv.tar
mkdir layers && cd layers
tar -xf ../iptv-4gtv.tar
```

### 3. 反編譯 .so 檔案
```bash
# 方法 A: 使用 pycdc (推薦)
pip3 install pycdc
pycdc app.cpython-312-x86_64-linux-musl.so > decompiled.py

# 方法 B: 使用 Ghidra (GUI)
# 下載 Ghidra, 開啟 .so 檔案, 執行 Python 反編譯

# 方法 C: Retdec 線上服務
# https://retdec.com 
# 上傳 app.cpython-312-x86_64-linux-musl.so
```

### 4. 驗證重建程式
```bash
# 比較你的倉庫與反編譯結果
diff -r /path/to/your/repo /reconstructed/code
```

## 立即可用的重建版本

現在已經在 `/tmp/4gtv_complete/complete_app.py` 

啟動方式：
```bash
cd /tmp/4gtv_complete
uvicorn complete_app:app --host 0.0.0.0 --port 5050
```

## 核心函式對照

來自 DWARF 分析的完整函式列表：

### FourGTVClient (4GTV API 客戶端)
- `get_dynamic_header_key()` - 取得動態認證 Header
- `fourgtv_auth()` - 4GTV 認證
- `get_channel_async()` - 非同步取得頻道資料
- `get_channel_name_async()` - 取得頻道名稱
- `get_puid()` - 取得頻道 PUID
- `_get_play_urls_by_api()` - 從 API 取得播放 URL (0=TV, 1=APP)

### XrayManager (代理核心)
- `parse_vmess_url()` / `parse_vless_url()` / `parse_trojan_url()` - URL 解析
- `download_xray()` - 下載 Xray-core
- `start_xray_from_vmess_url()` - 啟動 vmess 代理
- `stop_xray()` - 停止代理

### MultiProxyManager (多代理管理)
- `load_servers()` - 載入代理伺服器
- `get_best_server()` - 選擇最佳線路
- `get_enabled_servers()` - 過濾啟用伺服器

### proxy_ts_async (TS 代理核心)
- `fetch_ts()` - 取得 TS 切片
- `generate()` - 生成 m3u8 回應

### 其他核心函式
- `decrypt_key()` - 解密金鑰
- `pkcs7_unpad()` - 去除 PKCS7 填充
- `get_shanghai_time()` - 取得上海時區時間
- `generate_secure_token()` - 生成 64 位安全 Token
- `get_device_id()` - 取得設備 ID

## 環境變數設定

```bash
ADMIN_USERNAME=admin
ADMIN_PASSWORD=***
PROXY_HOST=0.0.0.0
XRAY_PORT=1080
TS_PROXY_ENABLED=true
COMPAT_MODE=false
APP_STREAM_SOURCE=1
TV_STREAM_SOURCE=0
```