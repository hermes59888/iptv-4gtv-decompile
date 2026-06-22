# 推送至 GitHub 的指令
# 執行前請設定正確的 GITHUB_TOKEN

export GITHUB_TOKEN="你的_GITHUB_TOKEN"

cd /home/jr/iptv-4gtv

# 方法 1: 使用 gh CLI (如果已安裝)
if command -v gh &> /dev/null; then
    gh auth login --with-token <<< "$GITHUB_TOKEN"
    git remote set-url origin https://github.com/hermes59888/iptv-4gtv-decompile.git
    gh repo set-default hermes59888/iptv-4gtv-decompile
    git push -u origin master
else
    # 方法 2: 使用 HTTPS 認證
    git remote set-url origin https://x-access-token:$GITHUB_TOKEN@github.com/hermes59888/iptv-4gtv-decompile.git
    git push -u origin master
fi

echo "完成！倉庫: https://github.com/hermes59888/iptv-4gtv-decompile"