#!/usr/bin/env bash
# 发布脚本：重新打包插件 zip → 将 marketplace.json 中的 zip 地址固定到最新提交 → 推送
# 用法：bash scripts/release.sh
set -euo pipefail
cd "$(dirname "$0")/.."

REPO="yuanhang45127/kimi-code-plugins-markets"
BASE="https://ghproxy.net/https://raw.githubusercontent.com/$REPO"

# 1. 重新打包所有插件（kimi.plugin.json 位于 zip 根目录）
mkdir -p dist
rm -f dist/*.zip
for p in plugins/*/; do
  id=$(basename "$p")
  (cd "$p" && zip -qr "../../dist/$id.zip" .)
  echo "packed: dist/$id.zip"
done

# 2. 提交插件与 zip 的变更（如有）
git add dist plugins
if ! git diff --cached --quiet; then
  git commit -m "chore: rebuild plugin zips"
fi

# 3. 把 marketplace.json 里的 zip 地址固定到当前提交（避免代理缓存旧内容）
SHA=$(git rev-parse HEAD)
sed -i '' -E "s|$BASE/[0-9a-f]{40}/dist/|$BASE/$SHA/dist/|g" marketplace.json
git add marketplace.json
if ! git diff --cached --quiet; then
  git commit -m "chore: pin plugin zip URLs to $SHA"
fi

# 4. 推送到两个远端
git push github main
git push origin main

NEW_SHA=$(git rev-parse HEAD)
echo
echo "发布完成。市场地址（固定到最新提交，复制到 Kimi Code 使用）："
echo "/plugins marketplace $BASE/$NEW_SHA/marketplace.json"
