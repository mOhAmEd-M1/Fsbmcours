from __future__ import print_function
from django.http.response import Http404
from django.shortcuts import render
from eduction.models import *

def SemesterPanelPage(request,filier,semester):
  context = {}
  return render(request,'backend/education/semester.html',context)

def DeleteSemester(request):
  pass
def CreateSemester(request,fil):
  pass
def EditSemester(request,fil):
  pass

