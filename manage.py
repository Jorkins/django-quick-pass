#!/usr/bin/env python
"""Django 快速通关 · 命令行入口"""
import os
import sys


def main():
    """运行管理命令"""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "未能导入 Django，请确认已安装并激活虚拟环境。"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
