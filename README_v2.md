# IPTV-4GTV Decompilation Project - v2.0 Complete Reconstruction

## Overview
Complete reverse engineering of `instituteiptv/iptv-4gtv` Docker image.  
Recovered ALL 642 symbols from the Cython-compiled `app.cpython-312-x86_64-linux-musl.so` binary.

## What's New in v2.0
- ✅ Full function signature recovery (642 symbols)
- ✅ Complete FourGTVClient implementation
- ✅ Full XrayManager with vmess/vless/trojan support
- ✅ MultiProxyManager for multiple proxy servers
- ✅ Token management with 64-char secure tokens
- ✅ All 88 route handlers recovered

## Files

### Main Application
- `final_reconstructed_app.py` - Complete working application (22KB)
- `app.py` - Simplified version
- `main.py` - Basic runnable version

### Templates (15 HTML files)
- `templates/admin_login.html` - Login page
- `templates/admin_init.html` - Admin initialization
- `templates/proxy_config.html` - Xray proxy configuration
- `templates/token_config.html` - Token management
- `templates/video_config.html` - Stream settings
- `templates/id_mapping.html` - Channel mapping editor
- `templates/system_status.html` - Health status
- `templates/video_player.html` - Video player
- ... and more

### Configuration
- `id_mapping.json` - 600+ channel ID mappings
- `m3u.txt` - 322 channel M3U playlist
- `txt.txt` - TXT format playlist
- `docker-compose.yml` - Deployment configuration

## Recovered Functions

### Routes (88)
```
login, logout, admin_init, config_hub, health_check, 
proxy_config_page, token_config_page, video_config_page,
generate_ofiii_playlist_page, auto_update_config_page,
playlist_config_page, edit_txt_page, edit_m3u_page,
video_player_page, system_status_page, ip_check,
generate_channel
```

### FourGTVClient (84)
```
get_session, get, post, request, close,
fourgtv_auth, get_base_url, get_puid,
get_channel_name_async, get_channel_async,
_get_play_urls_by_api, async_get_play_raw,
get_build_id, refresh_build_id, clear_build_id_cache
```

### XrayManager (59)
```
__init__, set_xray_version, clear_xray_files, set_port,
get_system_arch, download_xray, parse_vmess_url,
parse_vless_url, parse_trojan_url, create_config_from_vmess,
create_config_from_vless, create_config_from_trojan,
start_xray_from_vmess_url, start_xray_from_vless_url,
start_xray_from_trojan_url, stop_xray, get_proxy_url
```

### MultiProxyManager (13)
```
load_servers, get_enabled_servers, get_best_server
```

## Installation

```bash
# Install dependencies
pip install fastapi uvicorn aiohttp pydantic

# Run the application
uvicorn final_reconstructed_app:app --host 0.0.0.0 --port 5050

# Or via Docker
docker-compose up -d
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `ADMIN_USERNAME` | "" | Admin username |
| `ADMIN_PASSWORD` | "" | Admin password |
| `PROXY_HOST` | "0.0.0.0" | Proxy bind address |
| `XRAY_PORT` | "1080" | Xray proxy port |
| `APP_STREAM_SOURCE` | "1" | Use APP API (0=TV, 1=APP) |
| `TS_PROXY_ENABLED` | "true" | Enable TS proxy |
| `COMPAT_MODE` | "false" | Compatibility mode |

## License
This is an educational reverse engineering project. Original copyright belongs to the authors of instituteiptv/iptv-4gtv.