"""任务模型 —— 核心业务示例，用于演示 ORM、缓存、异步任务"""
from django.db import models
from django.conf import settings


class Task(models.Model):
    PRIORITY_CHOICES = [
        ("low", "低"),
        ("medium", "中"),
        ("high", "高"),
    ]
    STATUS_CHOICES = [
        ("pending", "待处理"),
        ("in_progress", "进行中"),
        ("completed", "已完成"),
        ("cancelled", "已取消"),
    ]

    title = models.CharField(max_length=200, verbose_name="标题")
    description = models.TextField(blank=True, verbose_name="描述")
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default="medium", verbose_name="优先级")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending", verbose_name="状态")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tasks",
        verbose_name="负责人",
    )
    due_date = models.DateTimeField(null=True, blank=True, verbose_name="截止时间")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = "tasks_task"
        ordering = ["-created_at"]
        verbose_name = "任务"
        verbose_name_plural = "任务"
        indexes = [
            models.Index(fields=["status", "priority"]),
            models.Index(fields=["owner", "-created_at"]),
        ]

    def __str__(self):
        return self.title
