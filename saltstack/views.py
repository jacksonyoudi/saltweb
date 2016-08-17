# Create your views here.
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from django.core.mail import send_mail


def  sshhtml(request):
    return render(request,'ssh.html')

def  indexhtml(request):
    return render(request,'index.html')

def  monitorhtml(request):
    return render(request,'monitor.html')


def  zabbixhtml(request):
    return render(request,'zabbix.html')

def  salthtml(request):
    return render(request,'salt.html')

def  opshtml(request):
    return render(request,'ops.html')

def  adminhtml(request):
    return render(request,'admin.html')
