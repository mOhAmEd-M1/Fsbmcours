from django.forms import ModelForm
from django import forms
from django.shortcuts import render

from courses.models import *
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Filier
        fields = (
            'name',
            'title'
        )

class semesterModelForm(forms.Form):
    FILIER_CHOICES = (
        ('Physique', 'Physique'),
        ('Chimie', 'Chimie'),
        ('Informatique','Informatique'),
        )
    name = forms.CharField(max_length=122)
    filierName = forms.ChoiceField(choices= FILIER_CHOICES)
    

class moduleModelForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = (
            'name',
        ) 

class CoursesModelFormviews(ModelForm):
    class Meta:
        model = Courses
        fields = (
            'name',
            'C_type',
            'pdf',
        ) 
    

