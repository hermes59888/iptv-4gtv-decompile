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
- admin_init
- admin_login_check
- check_auth
- get_playlist_files
- get_playlist_content
- save_m3u / save_txt / save_ofiii_m3u / save_ofiii_txt
- update_token
- load_token_config / save_token_config
- load_proxy_config / save_proxy_config
- get_proxy_servers / update_proxy_servers
- test_proxy_latency
- proxy_ts_async.fetch_ts
- create_proxy_connector
- XrayManager.start_proxy_from_server

## Python 相依套件
fastapi==0.136.3, hypercorn==0.18.0, aiohttp==3.14.1, apscheduler==3.11.2,
requests==2.34.2, beautifulsoup4==4.15.0, pycryptodome==3.23.0, pydantic==2.13.4

## 預設指令
CMD: ["sh", "-c", "export PORT=${PORT:-5050} && hypercorn app:app --bind 0.0.0.0:$PORT"]

## 環境變數
PROXY_HOST=0.0.0.0, XRAY_PORT=1080 (預設)
