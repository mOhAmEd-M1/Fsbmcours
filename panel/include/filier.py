from __future__ import print_function
from django.http.response import Http404
from eduction.models import *
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.decorators import login_required
import datetime
from itertools import chain
from django.core.paginator import Paginator , PageNotAnInteger, EmptyPage
from django.contrib import messages


def FilierPanelPage(request,filier):
  try:
    q_fil = Filier.objects.get(name = filier)
    context = {
    'Q_filier':q_fil,
    'Filiers':Filier.objects.all(),
    'Semmesters':Semester.objects.all(),
    'modulesn':Module.objects.all(),

    'Semesters':Semester.objects.filter(filierId = q_fil.pk),
    'SM':Semester.objects.filter(filierId = q_fil.pk),

    }
  except:
    print("not oki")
    raise Http404()
  return render(request,'backend/education/filier.html',context)
  
def DeleteFilier(request,filier):
  # try:
  query_set = Filier.objects.get(name = filier)
  print("filier is oki")
  query_set_Semester = Semester.objects.filter(filierId = query_set.pk)
  print("semester is oki")

  query_set_module = Module.objects.filter(filierid = query_set.pk)
  print("module is oki")
  if query_set_module:
    query_set_module.delete()
  if query_set_Semester:
    query_set_Semester.delete()
  query_set.delete()
  print(f"{query_set.name} is deleted succusful !!")
 
  return redirect('filierpnelPage')

  # except:
  #   print("not oki")
  #   raise Http404()
  # return render(request,'backend/delete.html',context)

def CreateFilier(request):
  pass
def EditFilier(request):
  pass


