from __future__ import print_function
from django.http.response import Http404
from django.shortcuts import render
from eduction.models import *


def ModulePanelPage(request):
  try:
    context = {
    'Q_filier':Filier.objects.all(),
    'Filiers':Filier.objects.all(),
    'Semmesters':Semester.objects.all(),
    'modulesn':Module.objects.all(),

    'Semesters':Semester.objects.all(),
    'SM':Semester.objects.all(),
    }
  except:
    print("not oki")
    raise Http404()
  return render(request,'backend/education/modl.html',context)

def Deletemodl(request):
  pass
def Createmodl(request):
  pass
def Editmodl(request):
  pass

