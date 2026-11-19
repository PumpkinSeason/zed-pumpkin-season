#!/bin/sh
# Installs the Pumpkin Season theme for Zed.
set -e

dest="$HOME/.config/zed/themes"
mkdir -p "$dest"
cp "$(dirname "$0")/themes/pumpkin-season.json" "$dest/"

echo "Installed to $dest"
echo "Open the theme selector (cmd-k cmd-t) and choose Pumpkin Season."
