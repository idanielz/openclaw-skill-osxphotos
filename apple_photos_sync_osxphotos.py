#!/usr/bin/env python3
"""
Apple Photos 大文件同步脚本
- 不删除相册，只增量添加
- osxphotos 会自动处理去重
"""

import subprocess
import re

OSX = "python3"

def restart_photos():
    subprocess.run(["pkill", "-9", "Photos"], capture_output=True)
    import time; time.sleep(2)
    subprocess.run(["open", "-a", "Photos"], capture_output=True, timeout=10)

def main():
    print("=== Apple Photos 大文件同步 ===")
    
    print("\n[1/3] 同步大图片 (>20MB)...")
    cmd = [OSX, "-m", "osxphotos", "query", "--min-size", "20MB", 
           "--only-photos", "--not-hidden", "--add-to-album", "大图片管理"]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    match = re.search(r"Adding (\d+)", result.stdout + result.stderr)
    print(f"   添加 {match.group(1) if match else 0} 张")
    
    print("\n[2/3] 同步大视频 (>300MB)...")
    cmd = [OSX, "-m", "osxphotos", "query", "--min-size", "300MB",
           "--only-movies", "--not-hidden", "--add-to-album", "大视频管理"]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    match = re.search(r"Adding (\d+)", result.stdout + result.stderr)
    print(f"   添加 {match.group(1) if match else 0} 个")
    
    print("\n[3/3] 重启 Photos...")
    restart_photos()
    
    print("\n=== 同步完成 ===")

if __name__ == "__main__":
    main()