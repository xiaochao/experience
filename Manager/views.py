# -*- coding: utf-8 -*-
# Create your views here
from django.shortcuts import render_to_response
from Manager.forms import RegisteForm,LoginForm
from Manager.models import User
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError


@csrf_exempt
def Registe(request):
    errors = ''
    if request.method == 'POST':
        form = RegisteForm(request.POST)
        if form.is_valid():
            context = form.cleaned_data
            p1 = User(name=context['name'], email=context['email'], password=context['password'])
            try:
                p1.save()
            except IntegrityError:
                errors = '用户已经存在'
    else:
        form = RegisteForm()

    return render_to_response('registe.html', {'form': form, 'errors': errors})

@csrf_exempt
def Login(request):
    errors = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            context = form.cleaned_data
            try:
                if '@' in context['name']:
                    id = User.objects.get(email=context['name'], password=context['password'])
                else:
                    id = User.objects.get(name=context['name'], password=context['password'])
                if not id:
                    errors = '用户名或者密码错误'
            except:
                errors = '登陆失败'
    else:
        form = LoginForm()
    return render_to_response('login.html', {'form': form, 'errors': errors})
