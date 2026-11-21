"""Django 快速通关 · 总路由分发"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    # 用户模块（认证、权限）
    path("api/users/", include("apps.users.urls")),
    # 任务模块（核心业务示例）
    path("api/tasks/", include("apps.tasks.urls")),
    # DRF 可浏览 API 登录
    path("api-auth/", include("rest_framework.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
