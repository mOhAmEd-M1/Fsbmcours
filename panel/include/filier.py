from __future__ import print_function
from django.http.response import Http404
from django.shortcuts import render
from eduction.models import *

def FilierPanelPage(request,filier):
  print("0")

  try:
    print("1")
    q_fil = Filier.objects.get(name = filier)
    print(f"-----{q_fil.name}")
    print("2")
    
    # print(f"-----{Semester.objects.get(filierId = q_fil.pk).name}")
    print("3")
    context = {
    'Q_filier':q_fil,
    'Filiers':Filier.objects.all(),
    'Semmesters':Semester.objects.all(),
    'modulesn':Module.objects.all(),


    'Semesters':Semester.objects.filter(filierId = q_fil.pk),
    }
  except:
    print("not oki")
    raise Http404()
  return render(request,'backend/education/index.html',context)
  
def DeleteFilier(request):
  pass
def CreateFilier(request):
  pass
def EditFilier(request):
  pass

