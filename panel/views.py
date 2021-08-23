from __future__ import print_function
from django.http.response import Http404
from django.shortcuts import render
from eduction.models import *
from panel.include.filier import *
from panel.include.semester import *
from panel.include.modl import *
# Create your views here.
def homepanel(request):
  context = {
    'Filiers':Filier.objects.all(),
    'Semmesters':Semester.objects.all(),
    'modulesn':Module.objects.all(),


    'SM':Semester.objects.all(),

  }
  return render(request,'backend/main/home.html',context)

def filierpnelPage(request,fil):
  context = {
    'Filiers':Filier.objects.all(),
    'Semmesters':Semester.objects.all(),
    'modulesn':Module.objects.all(),


    'SM':Semester.objects.all(),
  }
  return render(request,"backend/education/index.html",context)