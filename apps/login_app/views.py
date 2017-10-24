##########################################################################
#  LOGIN_APP - VIEWS.PY
##########################################################################
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

###[ LANDING PAGE ]###########################################################
def index(request):
    return render(request,'login_app/index.html')

###[ USER OPERATIONS ]########################################################
def create(request):
    #add a new user to the data base.  Vaidation happens in the model
    validationErrors = User.objects.validate_postData(request.POST)
    if validationErrors['status'] == False:
        userInfo = User.objects.create_user(request.POST)
        messages.success(request, 'User has been created.')
    else:
        for error in validationErrors['errors']:
            messages.error(request, error)
    return redirect('/')

def login(request):
    validationErrors = User.objects.validate_login(request.POST)
    if validationErrors['status'] == True:
        messages.error(request, 'Login Failed, please verifiy your email and password and try again.')
        return redirect('/')
    request.session['validated_user_email'] = validationErrors['user'].email
    request.session['validated_user_name'] = validationErrors['user'].fname
    request.session['validated_user_id'] = validationErrors['user'].id
    return redirect('/welcome')

def welcome(request):
    if 'validated_user_email' not in request.session:
        return redirect('/')

    context = {
        'validated_user' : User.objects.get(id=request.session['validated_user_id'])
    }

    return render(request,'login_app/welcome.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')
