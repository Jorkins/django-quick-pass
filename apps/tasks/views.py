from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Task
from .serializers import TaskSerializer


def task_list(request):
    """模板渲染：任务列表"""
    tasks = Task.objects.select_related("owner").all()[:20]
    return render(request, "tasks/list.html", {"tasks": tasks})


class TaskViewSet(viewsets.ModelViewSet):
    """DRF API：任务增删改查"""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
