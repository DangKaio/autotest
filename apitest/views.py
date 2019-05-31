from django.shortcuts import render
from django.http import  HttpResponseRedirect,HttpResponse#加入引用
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate,login
from apitest.models import Api_Test_Case,Api_Test_Step
# Create your views here.


def login(request):
    """实现登录功能"""
    if request.POST:
        username = password = ""
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            request.session['user'] = username
            response = HttpResponseRedirect('/home/')
            return response
        else:
            return render(request, 'login.html', {'error': 'username or password error'})
    return render(request, 'login.html')


def home(request):
    """登录主页"""
    return render(request, 'home.html')


def logout(request):
    """退出登录"""
    auth.logout(request)
    return render(request, 'login.html')

def apitest_manage(request):
    apitest_list=Api_Test_Case.objects.all()
    username=request.session.get('user','')
    return render(request,"apitest_manage.html",{"user":username,"apitests":apitest_list})
