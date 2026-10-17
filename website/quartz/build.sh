#!/usr/bin/env bash
# Build the Night Post example vault (examples/creative) as a Quartz site.
#   build.sh <output-dir>   build static files, e.g. website/site/night-post
#   build.sh --serve        preview at http://localhost:8080
set -euo pipefail

QUARTZ_VERSION=v4.5.2
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$HERE/../.." && pwd)"
WORK="$HERE/.quartz"
VAULT="$REPO/examples/creative"

if [ ! -d "$WORK" ]; then
  git clone --quiet --depth 1 --branch "$QUARTZ_VERSION" https://github.com/jackyzha0/quartz.git "$WORK"
fi
cp "$HERE/quartz.config.ts" "$HERE/quartz.layout.ts" "$WORK/"
[ -d "$WORK/node_modules" ] || (cd "$WORK" && npm ci --silent)

# Stage the vault as Quartz content; the README becomes the home page.
rm -rf "$WORK/content"
rsync -a --exclude .claude --exclude .obsidian --exclude .gitignore "$VAULT/" "$WORK/content/"
mv "$WORK/content/README.md" "$WORK/content/index.md"

cd "$WORK"
if [ "${1:-}" = "--serve" ]; then
  npx quartz build --serve -d content
else
  OUT="$(cd "$REPO" && mkdir -p "${1:?usage: build.sh <output-dir> | --serve}" && cd "$1" && pwd)"
  npx quartz build -d content -o "$OUT"
fi
