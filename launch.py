import os
import socket
from Utils.setUp import setUp
from Utils.config import config,loadConfig
from Utils.config import loadConfig
from django.core.management import execute_from_command_line
from Sercer.CustomerManage import customer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DataManager.settings')

def run():
    loadConfig()
    setUp()
    ip = "0.0.0.0:8001"
    execute_from_command_line(["./manage.py", "runserver", ip])

if __name__ == '__main__':
    run()