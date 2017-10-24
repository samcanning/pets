# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from ..login_app.models import User
from .models import Pet, Type
from django.contrib import messages

# Create your views here.
def index(request):
    if 'validated_user_email' not in request.session:
        return redirect('/')
    context = {
        'userpets': User.objects.get(id=request.session['validated_user_id']).pets.all(),
        'otherusers': User.objects.exclude(id=request.session['validated_user_id']).all(),
    }
    return render(request, 'pets_app/index.html', context)

def add(request):
    if 'validated_user_email' not in request.session:
        return redirect('/')
    context = {
        'type_list' : Type.objects.all(),
    }
    return render(request, 'pets_app/add_pet.html', context)

def create(request):
    if 'validated_user_email' not in request.session:
        return redirect('/')
    errors = Pet.objects.validate_postData(request.POST)
    if errors:
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags='create')
        return redirect('/pets/add')
    else:
        newPet = Pet.objects.create_pet(request.POST)
        newPet.owners.add(User.objects.get(id=request.session['validated_user_id']))
    return redirect('/pets')

def show(request, user_id):
    if 'validated_user_email' not in request.session:
        return redirect('/')
    context = {
        'user': User.objects.get(id=user_id),
        'userpets': User.objects.get(id=user_id).pets.all(),
    }
    return render(request, 'pets_app/show_user.html', context)

def delete(request, pet_id):
    if 'validated_user_email' not in request.session:
        return redirect('/')
    Pet.objects.get(id=pet_id).delete()
    return redirect('/pets')