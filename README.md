# Django 快速通关 · 配套代码仓库

本仓库配合《Django 快速通关》系列文章使用，从环境搭建到生产级部署，逐关通关。

## 快速开始

```bash
# 1. 克隆仓库
git clone https://github.com/Jorkins/django-quick-pass.git
cd django-quick-pass

# 2. 创建虚拟环境
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

# 3. 安装依赖
pip install -r requirements.txt

# 4. 数据库迁移
cd config
python manage.py migrate

# 5. 创建超级管理员
python manage.py createsuperuser

# 6. 运行开发服务器
python manage.py runserver
```

访问：http://127.0.0.1:8000/  及  http://127.0.0.1:8000/admin/

## 参考开源项目

- [Zulip](https://github.com/zulip/zulip) — 大型实时聊天系统（异步、权限、缓存参考）
- [mars-mgn](https://github.com/david-zlj/mars-mgn) — Django + DRF + Vue3 企业后台
- [seapagan/django-projects](https://github.com/seapagan/django-projects) — Django 5.1 + Tailwind + HTMX
- [RealWorld](https://github.com/thinkster/edu-django) — Django 规范示例
- [django-bolt](https://github.com/dj-bolt/django-bolt) — 基于 Rust 的高性能 Django

## 关注作者

![关注作者](docs/images/wechat-follow-banner.svg)
