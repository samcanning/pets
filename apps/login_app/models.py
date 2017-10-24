# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re, bcrypt

class UserManager(models.Manager):
    ###[ Validation for Users attempting to login to the site] ########################################################
    def validate_login(self, postData):
        validationErrors = {'status': False, 'errors': [], 'user': None}
        users = self.filter(email = postData['email'])
        if len(users) < 1: #if returned list of users is not empty the email already exists in the system
            validationErrors['status'] = True
        else:
            if bcrypt.checkpw(postData['password'].encode(), users[0].password.encode()):
                validationErrors['user'] = users[0]
            else:
                validationErrors['status'] = True
        return validationErrors

    ###[ Validations for data submitted by the user from registration page ]###########################################
    def validate_postData(self, postData):
        validationErrors = {'status': False, 'errors': [] }
        if len(postData ['fname']) < 2:
            validationErrors['errors'].append('First name needs to be at least 2 characters')
            validationErrors['status'] = True
        if len(postData ['lname']) < 2:
            validationErrors['errors'].append('Last name needs to be at least 2 characters')
            validationErrors['status'] = True
        if not re.match("[^@]+@[^@]+\.[^@]+", postData['email']):
            validationErrors['errors'].append('Email address does not appear to be valid')
            validationErrors['status'] = True
        if postData ['password'] != postData['c_password']:
            validationErrors['errors'].append('You passwords does not match.')
            validationErrors['status'] = True
        if len(postData['password']) < 5:
            validationErrors['errors'].append('A password needs to be 5 or more characters!')
            validationErrors['status'] = True
        if len(self.filter(email = postData['email'])) > 0:
            validationErrors['errors'].append('User already exists.')
            validationErrors['status'] = True
        return  validationErrors

    ###[ Add a new user to the database ]##############################################################################
    def create_user(self, postData):
        user = self.create(fname = postData['fname'], lname = postData['lname'], email = postData['email'], password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()))
        return user

class User(models.Model):
    fname = models.CharField(max_length=64)
    lname = models.CharField(max_length=64)
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    objects = UserManager()

    def __str__(self):
        return "id:{} name:{}{}".format(self.id,self.fname,self.lname   )