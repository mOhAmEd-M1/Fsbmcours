from __future__ import unicode_literals
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
import os
import uuid
import random
from datetime import datetime


def user_directory_path(instance,filename):
    # Get Current Date
    todays_date = datetime.now()
    month = todays_date.month
    if month == 1:
        month = 'January'
    elif month == 2:
        month = 'February'
    elif month == 3:
        month = 'March'
    elif month == 4:
        month = 'April'
    elif month == 5:
        month = 'May'
    elif month == 6:
        month = 'June'
    elif month == 7:
        month = 'July'
    elif month == 8:
        month = 'August'
    elif month == 9:
        month = 'September'
    elif month == 10:
        month = 'October'
    elif month == 11:
        month = 'November'
    elif month == 12:
        month = 'December'
    path =f"{todays_date.year}/Course/pdf/"
    extension = "." + filename.split('.')[-1]
    stringId = str(uuid.uuid4())
    randInt = str(random.randint(0, 9))

    # Filename reformat
    filename_reformat = stringId + randInt + extension

    return os.path.join(path, filename_reformat)
class Filier(models.Model):
    name = models.CharField(max_length=30, default='')
    title = models.CharField(max_length=40)
    count = models.IntegerField(default=0)
    show = models.IntegerField(default=0)
    class Meta:
        ordering = ["name"]
    def __str__(self):
        return self.name + f" {self.id}" 

    def filier_list(self):
        return reverse('front-semester-list', kwargs={'filier':self.name})
    # backend Functions
   
class Semester(models.Model):
    name = models.CharField(max_length=150)
    count = models.IntegerField(default=0)
    filierId = models.IntegerField(default=0)
    show = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    def __str__(self):
        return self.name   
        
    def save(self, *args, **kwargs):

        if self.slug == None:
            slug = slugify(self.name)
            self.slug = slug
       
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['name']

    def module_list(self):
        filier__qs = Filier.objects.get(pk = self.filierId) 
        return reverse('front-module-list', kwargs={ 'filier':filier__qs.name ,'semester':self.slug})
    # backend Functions

class Module(models.Model):
    name = models.CharField(max_length=150)
    semmesterid = models.IntegerField(default=0,null=True, blank=True)
    filierid = models.IntegerField(default=0,null=True, blank=True)
    ccount = models.IntegerField(default=0)
    Tdcount = models.IntegerField(default=0)
    tpcount = models.IntegerField(default=0)
    ecount = models.IntegerField(default=0)
    show = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    def save(self, *args, **kwargs):

        if self.slug == None:
            slug = slugify(self.name)
            self.slug = slug
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["name"]
    def __str__(self):
        return  self.name  


    def course_list(self):
        filier__qs = Filier.objects.get(pk = self.filierid)
        semester__qs = Semester.objects.get(pk=self.semmesterid)
        return reverse('front-course-list',kwargs={'filier':filier__qs.name,'semester':semester__qs.slug,'modl':self.slug})
    # backend Functions

class Courses(models.Model):
    CATEGORY_CHOICES = [
        ('cours','cours'),
        ('Traveaux derigie','Traveaux derigie'),
        ('Traveaux pratique','Traveaux pratique'),
        ('exam','exam')
    ]

    C_type =models.CharField(max_length=200, choices = CATEGORY_CHOICES , default='choices ...')
    name = models.CharField(max_length=150)
    moduleid = models.IntegerField(default=0)
    semesterid = models.IntegerField(default=0)
    filierid = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True, null=True)
    pdf = models.FileField(upload_to=user_directory_path)
    class Meta:
        ordering = ["name"]
    def __str__(self):
        return "%s %s %s" % (self.name, self.semesterid, self.moduleid)
    # backend Functions :
