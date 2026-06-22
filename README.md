# IPTV-4GTV Decompile Project

## Overview
This project contains the reverse-engineered structure and configuration of the `instituteiptv/iptv-4gtv` Docker image for educational purposes.

## Contents
- `decompile/` - Extracted Docker image layers and reconstructed filesystem
- `decompile/rootfs/` - Complete file system extracted from the image
- `decompile/analysis-report.md` - Analysis report of the image structure
- `docker-compose.yml` - Docker Compose configuration for running the service

## Key Findings

### Application Structure
- **Main binary**: `app.cpython-312-x86_64-linux-musl.so` - Cython-compiled Python module (8MB)
- **Templates**: 14 HTML templates for admin interface
- **Configuration**: `id_mapping.json` maps 4GTV channel IDs to internal stream IDs
- **Playlists**: M3U playlist (322 channels) and TXT format playlist

### Technology Stack
- Python 3.12.13 on Alpine Linux
- FastAPI + Hypercorn ASGI server
- Async HTTP with aiohttp
- APScheduler for task scheduling
- PySocks for proxy support

### Endpoints (from binary analysis)
- `/admin/init` - Admin initialization
- `/login` - Authentication
- `/playlist` - M3U playlist generation
- `/proxy/*`, `/ts-proxy/*` - Streaming proxy endpoints
- `/config/*` - Configuration pages

## Usage

### Quick Deploy
```bash
docker run -d \
  --name iptv-4gtv \
  -p 50007:5050 \
  --restart=always \
  instituteiptv/iptv-4gtv:latest
```

### Via Docker Compose
```bash
docker-compose up -d
```

## Analysis Report
See `decompile/analysis-report.md` for full details.

## Disclaimer
This is an educational reverse-engineering project. All content belongs to their respective owners.
