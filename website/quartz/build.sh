#!/usr/bin/env bash
# Build the Night Post example vault (examples/creative) as a Quartz site.
#   build.sh <output-dir>   build static files, e.g. website/site/night-post
#   build.sh --serve        preview at http://localhost:8080
set -euo pipefail

# Quartz v4.5.2, pinned by commit so a moved tag can't change what runs.
QUARTZ_COMMIT=4923affa7722dfc751f1074348e6dad214fe0c08
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$HERE/../.." && pwd)"
WORK="$HERE/.quartz"
VAULT="$REPO/examples/creative"

if [ ! -d "$WORK" ]; then
  git init --quiet "$WORK"
  git -C "$WORK" fetch --quiet --depth 1 https://github.com/jackyzha0/quartz.git "$QUARTZ_COMMIT"
  git -C "$WORK" checkout --quiet FETCH_HEAD
fi
if [ "$(git -C "$WORK" rev-parse HEAD)" != "$QUARTZ_COMMIT" ]; then
  echo "Quartz checkout is not at $QUARTZ_COMMIT; delete $WORK and rerun." >&2
  exit 1
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
