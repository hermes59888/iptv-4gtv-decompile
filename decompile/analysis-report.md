# IPTV-4GTV Docker Image Decompile Report

## 映像資訊
- **映像名稱**: instituteiptv/iptv-4gtv:latest
- **基底系統**: Alpine Linux (3.24.0)
- **Python 版本**: 3.12.13
- **暴露端口**: 5050/tcp, 1080/tcp

## 目錄結構
```
/app/
├── app.cpython-312-x86_64-linux-musl.so  (8.0 MB, compiled extension module)
├── config/
│   └── id_mapping.json                   (4GTV 頻道ID對照表, 1293 行)
├── templates/                            (14 個 HTML 模板)
│   ├── admin_init.html
│   ├── admin_login.html
│   ├── config_hub.html
│   ├── edit_m3u.html
│   ├── edit_ofiii_m3u.html
│   ├── edit_ofiii_txt.html
│   ├── edit_txt.html
│   ├── generate_ofiii_playlist.html
│   ├── id_mapping.html
│   ├── proxy_config.html
│   ├── system_status.html
│   ├── token_config.html
│   ├── video_config.html
│   └── video_player.html
├── m3u.txt                               (322 行 M3U 播放列表)
├── txt.txt                               (11K, 文字格式播放列表)
├── static/                               (靜態檔案)
└── xray/                                 (Xray 相關)

## 主要函式端點 (從 app.cpython-312 提取)

### 管理與認證
- `admin_init`, `admin_init_page` - 管理員初始化
- `login_page`, `login`, `logout` - 登入/登出
- `verify_super_admin` - 超級管理員驗證
- `api_auth_required`, `web_auth_required` - 認證裝飾器

### 播放清單
- `get_playlist_files` - 取得播放清單檔案
- `get_playlist_content` - 取得播放清單內容
- `save_m3u`, `save_txt` - 儲存 M3U/TXT 播放清單
- `generate_m3u_vod_content`, `generate_txt_vod_by_name` - 生成 VOD 內容
- `parse_m3u_content`, `process_m3u_content` - 解析 M3U 內容

### Token 與設定
- `load_token_config`, `save_token_config` - Token 設定
- `load_proxy_config`, `save_proxy_config` - 代理設定
- `load_unified_config`, `save_unified_config` - 統一設定
- `update_token`, `update_video_config` - 更新配置

### 代理系統 (Xray)
- `XrayManager.start_proxy_from_server` - 啟動代理
- `XrayManager.parse_vmess_url` - 解析 Vmess 網址
- `XrayManager.parse_vless_url` - 解析 Vless 網址
- `XrayManager.parse_trojan_url` - 解析 Trojan 網址
- `MultiProxyManager.get_best_server` - 取得最佳代理
- `test_proxy_latency` - 測試代理延遲

### 4GTV 客戶端
- `FourGTVClient.request`, `FourGTVClient.get`, `FourGTVClient.post` - HTTP 請求
- `fourgtv_auth` - 4GTV 認證
- `decrypt_key`, `pkcs7_unpad` - 金鑰解密
- `get_puid`, `get_channel_name_async` - 取得頻道資料

### 路由處理
- `root_handler` - 根路由處理
- `clear_build_id_cache_endpoint` - 清除建置快取
- `get_current_proxy_status` - 取得代理狀態
- `health_check`, `readiness_check` - 健康檢查

### 頁面路由 (從函式推測)
- `/admin/init` - 管理員初始化頁面
- `/login` - 登入頁面與認證
- `/playlist/m3u` - M3U 播放清單
- `/playlist/txt` - TXT 播放清單
- `/config/proxy` - 代理設定頁面
- `/config/token` - Token 設定頁面
- `/config/video` - 影片設定頁面
- `/proxy/ts` - TS 串流代理
- `/xray/*` - Xray 代理相關

### 4GTV/OFIII 相關
- `ofiii_get_playlist` - OFIII 播放清單
- `generate_ofiii_playlists` - 生成 OFIII 播放清單
- `play_4gtv` - 4GTV 撰放路由
- `extract_channel_details` - 提取頻道詳細資料

## Python 相依套件
fastapi==0.136.3, hypercorn==0.18.0, aiohttp==3.14.1, apscheduler==3.11.2,
requests==2.34.2, beautifulsoup4==4.15.0, pycryptodome==3.23.0, pydantic==2.13.4

## 預設指令
CMD: ["sh", "-c", "export PORT=${PORT:-5050} && hypercorn app:app --bind 0.0.0.0:$PORT"]

## 環境變數
PROXY_HOST=0.0.0.0, XRAY_PORT=1080 (預設)
