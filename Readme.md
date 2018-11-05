# Launch SKetch Web to OSS
## 介绍
本脚本可以自动将 Sketch 插件 Launchpad 生成的网页，托管到阿里云 OSS 上。

## Feature
* 自动修改生成网页的 html，去除多余代码，仅保留生成的网页代码；
* 自动将图片资源从 Amazon 服务器上下载并通过 TinyPNG 压缩；
* 将压缩后的文件上传到阿里云 OSS 上，以加快图片的访问速度；
* 自动将修改过后的 html 文件上传到 OSS 上，并生成访问链接。

## 使用
### 安装依赖库
通过 `pip3 install -r requirements.txt` 命令来安装依赖库。

### 注册 TinyPNG 和 Aliyun OSS
#### TinyPNG
注册地址：https://tinypng.com/developers

#### Aliyun OSS
* 注册阿里云账号，开通 OSS，创建一个托管 html 和图片等资源的 Bucket。
* 将 Bucket 设置为公开可读，这样别人才能访问你托管的网页。

### 配置 config
* 复制 `config_example.py` 文件并修改文件名为 `config.py`
* 打开 `config.py` 文件，将你创建的 OSS Bucket 相关信息填写到配置中
* 配置 TinPNG api
* 配置 OSS 文件夹，以方便管理你上传的文件和图片等资源
* 配置你从 Sketch 插件 Launchpad 生成的链接
* 配置生成的 html 文件的名字

```
# AliyunOSS access config
ACCESS_KEY_ID = ''
ACCESS_KEY_SECRET = ''
OSS_BUCKET_NAME = ''
OSS_ENDPOINT = ''

# TinyPNG config
TINIFY_KEY = ""
TINIFY_PROXY = ""


# OSS folder config
# If you have parent folder, add the parent folder name and "/" before the folder.
# Use ‘-’ to connect words.
# example:'imgs/product-intro-en'
html_oss_bucket_folder = ''
imgs_oss_bucket_folder = ''


# local temp folder
# After images and htmls has been uploadde, the temp files will be deleted.
temp_imgs_local_folder = 'temp_imgs'
temp_html_local_folder = 'temp_htmls'


# LaunchPad preview url
# example: 'https://launchpad.animaapp.com/preview/xxxxxxxx'
web_url = ''

# the name fo your html
web_name = ''

# the web title
title = ''
```

### 运行
通过命令 `sudo python3 main_func.py` 运行。

## TO-DO
- [ ] GUI：现在仅通过 Tinker 实现了基本的 GUI，但是存在 bug，可以通过 `gui.py` 查看。下一步打算通过 web 实现。
- [ ] 同时处理多个 Launchpad 生成的网页链接


