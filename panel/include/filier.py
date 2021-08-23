from __future__ import print_function
from django.db.models.query import QuerySet
from django.http.request import QueryDict
from django.http.response import Http404
from django.shortcuts import render
from eduction.models import *

def FilierPanelPage(request,filier):
  try:
    q_fil = Filier.objects.get(name = filier)
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
  return render(request,'backend/education/filier.html',context)
  
def DeleteFilier(request,fil):
  try:
    QuerySet = Filier.objects.get(name = fil)
    QuerySet_Semester = Semester.objects.get(filierId = QuerySet.pk)
    QuerySet_module = Module.objects.get(semmesterid = QuerySet_Semester.pk,filierid = QuerySet.pk)
    QuerySet_module.delete()
    QuerySet_Semester.delete()
    QuerySet.delete()
    context = {
      "filier":QuerySet,
      "semeter":QuerySet_Semester,
      "module":QuerySet_module,
    }
  except:
    print("not oki")
    raise Http404()
  return render(request,'backend/education/filier.html',context)
def CreateFilier(request):
  pass
def EditFilier(request):
  pass

