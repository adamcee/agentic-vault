#!/usr/bin/env bash

# Agentic Vault Initialization Script
# Copies the template to a target directory and initializes git.

set -e

if [ -z "$1" ]; then
  echo "Usage: ./init-vault.sh <target-directory>"
  exit 1
fi

TARGET_DIR="$1"
TEMPLATE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "Initializing Agentic Vault in $TARGET_DIR..."

# Create target directory
mkdir -p "$TARGET_DIR"

# Copy template contents (excluding .git if it exists, and the scripts folder)
rsync -av --exclude='.git' --exclude='scripts/' "$TEMPLATE_DIR/" "$TARGET_DIR/"

# Initialize git
cd "$TARGET_DIR"
git init
git add .
git commit -m "chore: initialize Agentic Vault"

echo "✅ Vault initialized successfully!"
echo "Next steps:"
echo "1. cd $TARGET_DIR"
echo "2. Open SYSTEM.md and fill in your project details."