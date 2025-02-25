#!/bin/bash

# 设置下载地址和目标路径
URL="https://storage.googleapis.com/chrome-for-testing-public/133.0.6943.126/linux64/chromedriver-linux64.zip"
TARGET_DIR="$HOME/tools"
ZIP_FILE="$TARGET_DIR/chromedriver-linux64.zip"

# 创建目标目录
mkdir -p "$TARGET_DIR"

# 下载 chromedriver，显示进度条
echo "Downloading chromedriver..."
wget --progress=bar:force:noscroll "$URL" -O "$ZIP_FILE"

# 解压 zip 文件
echo "Extracting chromedriver..."
unzip -q "$ZIP_FILE" -d "$TARGET_DIR"

# 设置 chromedriver 可执行权限
echo "Setting executable permissions..."
chmod +x "$TARGET_DIR/x"

# 清理 zip 文件
echo "Cleaning up..."
rm "$ZIP_FILE"

# 完成提示
echo "Chromedriver installation complete!"
