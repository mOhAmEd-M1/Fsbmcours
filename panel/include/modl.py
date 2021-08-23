from __future__ import print_function
from django.http.response import Http404
from django.shortcuts import render
from eduction.models import *


def ModulePanelPage(request,filier,semester,modl):
  context = {}
  return render(request,'backend/education/modl.html',context)

def Deletemodl(request):
  pass
def Createmodl(request):
  pass
def Editmodl(request):
  pass

