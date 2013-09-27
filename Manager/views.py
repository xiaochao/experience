# -*- coding: utf-8 -*-
# Create your views here
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, Http404
from Manager.forms import RegisteForm,LoginForm
from Manager.error import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from Manager.models import Bug
import time


@csrf_exempt
def Registe(request):
    errors = dict()
    if request.method == 'POST':
        form = RegisteForm(request.POST)
        if form.is_valid():
            context = form.cleaned_data
            user = User.objects.create_user(context['name'], context['email'], context['password'])
            try:
                user.save()
                return HttpResponseRedirect('/login')
            except:
                errors['exists'] = USER_EXISTS
        else:
            errors = form._errors
    else:
        form = RegisteForm()

    return render_to_response('registe.html', {'form': form, 'errors': errors, 'username':request.user.username})

@csrf_exempt
def Login(request):
    errors = dict()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            context = form.cleaned_data
            username = context['name']
            password = context['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_active:
                    return HttpResponseRedirect('/index', {'username':request.user.username})
                else:
                    errors['permission'] = '权限错误'
            else:
                errors['failed'] = '用户名或者密码错误'
    else:
        form = LoginForm()
    return render_to_response('login.html', {'form': form, 'errors': errors, 'username':request.user.username})

@csrf_exempt
def Index(request):
    error = dict()
    if request.method == 'POST':
        context = request.POST
        tt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        p = Bug(title=context['title'], explain=context['explain'], author=request.user.id, kind=1, time=tt)
        try:
            p.save()
            return HttpResponseRedirect('#')
        except:
            error['SubmitError'] = '提交失败了'

    bugs = Bug.objects.all()
    if str(request.user.username):
        login = True
    else:
        login = False
    return render_to_response('index.html', {'bugs': bugs, 'error':error, 'username':request.user.username, 'needlogin':login})

@csrf_exempt
def Logout(request):
    logout(request)
    return HttpResponseRedirect('/index')

@csrf_exempt
def BugDetail(request, id):
    error = dict()
    bug_id = id
    bug = Bug.objects.get(id='%s' % bug_id)
    return render_to_response('detail.html', {'error':error, 'bug':bug})