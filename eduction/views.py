from django.db.models import query
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404


from .models import *

# Create your views here.
def homepage(request):
  context = {
    'Filires':Filier.objects.all(),
    'semester':Semester.objects.all(),

    'Courses':Courses.objects.all().order_by('-pk')[:7],
    'Module':Module.objects.all(),
  }
  return render(request,'index.html',context)

def filier_Page(request,fil):
  try:
    context = {
    'Filires':Filier.objects.all(),
    'semester':Semester.objects.all(),
    'Courses':Courses.objects.filter(filierid = Filier.objects.get(name = fil).pk).order_by('-pk')[:7],
    'Module':Module.objects.filter(filierid = Filier.objects.get(name = fil).pk),

    'filire':Filier.objects.get(name = fil),
    'filireid':Filier.objects.get(name = fil).pk,
    'Semester':Semester.objects.filter(filierId = Filier.objects.get(name = fil).pk )
  }
  except:
    raise Http404()

  return render(request,'eduction/filier.html',context)


def semister_Page(request,fil,semester):
  q_fil = Filier.objects.get(name = fil)
  q_sem = Semester.objects.get(slug = semester,filierId = q_fil.pk)
  try:
    context = {
    'Filires':Filier.objects.all(),
    'semester':Semester.objects.all(),
    'Courses':Courses.objects.filter(filierid = q_fil.pk,semesterid = q_sem.pk).order_by('-pk')[:7],

    'filire':Filier.objects.get(name = fil),
    'Semmester':Semester.objects.get(slug = semester, filierId = Filier.objects.get(name = fil).pk ),

    'filireid':Filier.objects.get(name = fil).pk,
    'Semester':Semester.objects.filter(slug = semester, filierId = Filier.objects.get(name = fil).pk ),
    'Module':Module.objects.filter(semmesterid = Semester.objects.get(slug = semester, filierId = Filier.objects.get(name = fil).pk ).pk , filierid = Filier.objects.get(name = fil).pk )
    }
  except:
    context ={}
  
  return render(request,'eduction/semester.html',context)

def modulePage(request,fil,semester,modl):
  q_fil = Filier.objects.get(name = fil)
  qs_module = Module.objects.get(filierid = q_fil.pk,slug = modl)
  filierQuery = Filier.objects.get(name = fil)
  # q_semester = Semester.objects.filter(slug = semester)
  q_module =  Module.objects.filter(filierid = q_fil.pk,slug = modl)
  fileNumber = qs_module.ccount  + qs_module.Tdcount + qs_module.tpcount + qs_module.ecount
  context = {
    'module':q_module,

    'fileNumber':fileNumber,
    'Filires':Filier.objects.all(),
    'semester':Semester.objects.all(),
    'Module':Module.objects.filter(filierid = filierQuery.pk),
    'Courses': Courses.objects.filter(moduleid = Module.objects.get(filierid = q_fil.pk,slug = modl).pk,semesterid = Module.objects.get(filierid = q_fil.pk,slug = modl).semmesterid )
    }
  return render(request,'eduction/module.html',context)