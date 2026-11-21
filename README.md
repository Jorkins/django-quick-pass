# Django 快速通关 · 配套代码仓库

本仓库配合《Django 快速通关：架构与实战系列》文章使用，从入门到生产级部署，逐关通关。

## 系列进度（对应文章模块）

| 关卡 | 模块 | 对应目录 | 状态 |
|------|------|----------|------|
| 第 1-4 关 | 快速通关·起步 | `demo/` | 📋 待撰写 |
| 第 5-9 关 | 核心架构深入 | `core/` | 📋 待撰写 |
| 第 10-17 关 | 生产级后端架构 | `production/` | 📋 待撰写 |
| 第 18-21 关 | 前后端分离全栈 | `fullstack/` | 📋 待撰写 |
| 第 22-23 关 | 高性能与部署 | `deploy/` | 📋 待撰写 |

## 快速开始

```bash
# 1. 创建虚拟环境
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

# 2. 安装依赖
pip install -r requirements.txt

# 3. 数据库迁移
cd config
python manage.py migrate

# 4. 创建超级管理员
python manage.py createsuperuser

# 5. 运行开发服务器
python manage.py runserver
```

访问：http://127.0.0.1:8000/  及  http://127.0.0.1:8000/admin/

## 参考开源项目

- [Zulip](https://github.com/zulip/zulip) — 大型实时聊天系统（异步、权限、缓存参考）
- [mars-mgn](https://github.com/david-zlj/mars-mgn) — Django + DRF + Vue3 企业后台
- [seapagan/django-projects](https://github.com/seapagan/django-projects) — Django 5.1 + Tailwind + HTMX
- [RealWorld](https://github.com/thinkster/edu-django) — Django 规范示例
- [django-bolt](https://github.com/dj-bolt/django-bolt) — 基于 Rust 的高性能 Django
