# -*- coding: utf-8 -*-
# Create your views here
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from Manager.forms import RegisteForm,LoginForm
from Manager.error import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from Manager.models import Bug


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

    return render_to_response('registe.html', {'form': form, 'errors': errors})

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
                    return HttpResponseRedirect('/success.html')
                else:
                    errors['permission'] = '权限错误'
            else:
                errors['failed'] = '用户名或者密码错误'
    else:
        form = LoginForm()
    return render_to_response('login.html', {'form': form, 'errors': errors})

@csrf_exempt
def Index(self):
    bugs = Bug.objects.all()
    return render_to_response('index.html', {'bugs': bugs})

@csrf_exempt
def CreateBug(self):
    return