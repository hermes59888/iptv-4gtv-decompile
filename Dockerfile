FROM python:3.12-alpine

WORKDIR /app

# 安裝依賴
RUN pip install --no-cache-dir fastapi uvicorn jinja2 aiohttp pydantic apscheduler pycryptodome hypercorn

# 複製應用程式
COPY app/ ./app/
COPY decompile/rootfs/app/templates/ app/templates/
COPY decompile/rootfs/app/m3u.txt app/m3u.txt
COPY decompile/rootfs/app/txt.txt app/txt.txt
COPY decompile/rootfs/app/config/id_mapping.json app/config/id_mapping.json

# 建立必要目錄
RUN mkdir -p /app/templates /app/config

EXPOSE 5050 1080

ENV PORT=5050
ENV ADMIN_USER=admin
ENV ADMIN_PWD=password

CMD ["hypercorn", "app.main:app", "--bind", "0.0.0.0:5050"]