# osxphotos Skill

Apple Photos 管理工具，基于 [osxphotos](https://github.com/RhetTbull/osxphotos) 项目。

## 安装

```bash
/usr/local/opt/python@3.12/bin/python3.12 -m pip install osxphotos
```

## 核心功能

### CLI 命令

| 命令 | 功能 |
|------|------|
| `osxphotos query` | 查询照片 |
| `osxphotos export` | 导出照片 |
| `osxphotos sync` | 同步元数据 |
| `osxphotos batch-edit` | 批量编辑 |
| `osxphotos add-locations` | 添加位置 |
| `osxphotos orphans` | 查找孤立照片 |
| `osxphotos compare` | 比较库 |
| `osxphotos timewarp` | 调整时间 |

### 查询选项

```
--min-size 20MB        # 最小文件大小
--max-size 100MB      # 最大文件大小
--only-photos        # 只照片
--only-movies        # 只视频
--favorite           # 收藏
--edited / --not-edited
--burst              # 连拍
--from-date 2024-01-01
--has-location / --no-location
--duplicate         # 重复
--missing            # 缺失
--not-hidden         # 排除已删除
--add-to-album NAME  # 添加到相册
```

### 常用示例

```bash
# 查询大文件
osxphotos query --min-size 20MB --only-photos
osxphotos query --min-size 300MB --only-movies

# 导出
osxphotos export --min-size 20MB --output ~/Desktop/bigPhotos

# 批量添加到相册（相册会自动创建）
osxphotos query --min-size 20MB --add-to-album "大文件"

# 找孤立照片
osxphotos orphans

# 找重复
osxphotos query --duplicate
```

## 更新检查

项目地址：https://github.com/RhetTbull/osxphotos

在 skill 更新检查时检查是否有新版本。

```bash
# 检查版本
osxphotos version
```