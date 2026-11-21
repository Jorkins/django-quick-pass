"""Celery 任务示例 —— 发送任务完成通知"""
from celery import shared_task


@shared_task
def send_task_complete_notification(task_id, owner_email):
    """模拟异步发送邮件/通知"""
    print(f"[Celery] 任务 {task_id} 已完成，通知发送至 {owner_email}")
    return {"task_id": task_id, "status": "notified"}
