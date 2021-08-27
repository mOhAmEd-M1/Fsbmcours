from __future__ import print_function
from django.http.response import Http404
from django.shortcuts import render
from eduction.models import *

def SemesterPanelPage(request):
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
  return render(request,'backend/education/semester.html',context)

def DeleteSemester(request,fil,id):
  pass
def CreateSemester(request):
  pass

def EditSemester(request,fil,id):
  pass

