# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ..login_app.models import User
from django.contrib import messages

# Create your models here.
class PetManager(models.Manager):
    def validate_postData(self, postData):
        # validationErrors = {'status': False, 'errors': [] }
        validationErrors = {}
        if len(postData ['name']) < 2:
            validationErrors['name']='Name needs to be at least 2 characters.'
        if len(postData['newanimal']) > 0 and len(postData['animal']) > 0:
            validationErrors['type'] = 'Both fields cannot be used.'
        elif len(postData['newanimal']) == 0 and len(postData['animal']) == 0:
            validationErrors['type'] = 'Pet needs a type.'
        return  validationErrors

    ###[ Add a new user to the database ]##############################################################################
    def create_pet(self, postData):
        if len(Type.objects.filter(animal=postData['newanimal'])) > 0:
            pet = self.create(name = postData['name'], type=Type.objects.get(animal=postData['newanimal']))
            return pet
        if postData['newanimal'] != '':
            newType = Type.objects.create(animal = str.lower(str(postData['newanimal'])))
            pet = self.create(name = postData['name'], type = newType)
            return pet
        pet = self.create(name = postData['name'], type = Type.objects.get(id=postData['animal']))
        return pet


class Type(models.Model):
    animal = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Pet(models.Model):
    name = models.CharField(max_length=40)
    type = models.ForeignKey(Type, related_name='pets')
    owners = models.ManyToManyField(User, related_name='pets')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PetManager()
