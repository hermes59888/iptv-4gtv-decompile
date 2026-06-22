# IPTV-4GTV 反編譯專案

## 概述
本專案為教育目的用，包含對 `instituteiptv/iptv-4gtv` Docker 映像的逆向工程分析與結構提取。

## 內容
- `decompile/` - 解出的 Docker 映像層與重建的檔案系統
- `decompile/rootfs/` - 從映像中提取的完整檔案系統
- `decompile/analysis-report.md` - 映像結構分析報告
- `docker-compose.yml` - Docker Compose 部署配置

## 關鍵發現

### 應用程式結構
- **主程式**: `app.cpython-312-x86_64-linux-musl.so` - Cython 編譯的 Python 模組 (8MB)
- **範本檔**: 14 個 HTML 範本供管理介面使用
- **設定檔**: `id_mapping.json` 對應 4GTV 頻道 ID 與內部串流 ID
- **播放清單**: M3U 播放清單 (322 個頻道) 與 TXT 格式清單

### 技術堆疊
- Alpine Linux 上的 Python 3.12.13
- FastAPI + Hypercorn ASGI 伺服器
- aiohttp 非同步 HTTP
- APScheduler 任務排程
- PySocks 代理支援

### 端點 (從二進位分析提取)
- `/admin/init` - 管理員初始化
- `/login` - 認證登入
- `/playlist` - M3U 播放清單生成
- `/proxy/*`、`/ts-proxy/*` - 串流代理端點
- `/config/*` - 設定頁面

## 使用方法

### 快速部署
```bash
docker run -d \
  --name iptv-4gtv \
  -p 50007:5050 \
  --restart=always \
  instituteiptv/iptv-4gtv:latest
```

### 使用 Docker Compose
```bash
docker-compose up -d
```

## 分析報告
詳細內容請參閱 `decompile/analysis-report.md`。

## 免責聲明
本為教育研究用途的逆向工程專案，所有內容版權屬於原所有者。
