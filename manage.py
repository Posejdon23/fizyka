#!/usr/bin/env python3
import os
import sys
import pymysql

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fizyka.settings")

    from django.core.management import execute_from_command_line
    try:
        pymysql.install_as_MySQLdb()
    except ImportError:
        pass
    execute_from_command_line(sys.argv)
