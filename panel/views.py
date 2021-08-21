from django.shortcuts import render
from eduction.models import *
# Create your views here.
def homepanel(request):
  context = {
    'Filiers':Filier.objects.all(),
    'Semmesters':Semester.objects.all(),
    'modulesn':Module.objects.all(),
  }
  return render(request,'backend/main/home.html',context)

def FilierPanelPage(request):
  context = {}
  return render(request,'backend/education/index.html',context)