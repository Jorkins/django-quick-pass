"""用户模型 —— 参考 mars-mgn 企业级后台设计"""
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """自定义用户：扩展手机号、部门、角色"""
    phone = models.CharField(max_length=20, blank=True, verbose_name="手机号")
    department = models.CharField(max_length=50, blank=True, verbose_name="部门")
    role = models.CharField(
        max_length=20,
        choices=[("admin", "管理员"), ("editor", "编辑"), ("viewer", "访客")],
        default="viewer",
        verbose_name="角色",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = "users_user"
        verbose_name = "用户"
        verbose_name_plural = "用户"

    def __str__(self):
        return self.username
