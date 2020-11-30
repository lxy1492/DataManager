import os
import socket
from django.shortcuts import render
from django.shortcuts import HttpResponse,HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import redirect

from Utils.config import config

def index(request):
    ip = socket.gethostbyname(socket.getfqdn(socket.gethostname()))
    port = config["Port"]
    add = ip+":"+port
    add = "网站地址：http://"+add
    user = "未登录"
    HomeViewTitle = "MD_Data"
    hello = "扫码登陆服务器："
    return render(request,"home/index.html",{"title":"MD_Data","user":user,"ip":add,"hometitle":HomeViewTitle,"hello":hello})