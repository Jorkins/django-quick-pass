"""用户视图 —— 函数视图 + 类视图示例"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import User
from .serializers import UserSerializer


def user_list(request):
    """模板渲染：用户列表页面"""
    users = User.objects.all()[:20]
    return render(request, "users/list.html", {"users": users})


@login_required
def user_me(request):
    """当前登录用户信息"""
    return render(request, "users/me.html", {"user": request.user})


class UserViewSet(viewsets.ModelViewSet):
    """DRF API：用户增删改查"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
