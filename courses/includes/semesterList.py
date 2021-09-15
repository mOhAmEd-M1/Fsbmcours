from django.shortcuts import render
from courses.models import *
from django.http import Http404
from django.views import generic

re__path = "frontend/courses/"

def semester_list(request,filier):
  try:
    fil__qs = Filier.objects.get(name = filier)
  except :
    return Http404()
  context = {
    # query Header
    "Filires":Filier.objects.all(),
    # end 
    "filire":fil__qs,
    "Filiers":Filier.objects.filter(name = filier),
    "semester":Semester.objects.filter(filierId = fil__qs.id),
    "Courses":Courses.objects.filter(filierid = fil__qs.id),
  }
  return render(request,f'{re__path}/semisterList.html',context)




backendsemesterListPath = "backend/courses/semesterList/"
from courses.forms import semesterModelForm
from django.contrib import messages

def backendSemesetrList(request):
  context = {
    "Filires":Filier.objects.all(),
    "semester":Semester.objects.all(),
  }
  return render(request,f"{backendsemesterListPath}list.html",context)

def semesterCreateViews(request):
  if request.method or request.method == "POST":
    forms = semesterModelForm(request.POST or None)
    if forms.is_valid():
      name = forms.cleaned_data['name']
      filierName = forms.cleaned_data['filierName']
    
      qs__filier = Filier.objects.get(name = filierName)
      if len(Semester.objects.filter(filierId = qs__filier.id,name = name)) == 0 :
        Semester.objects.create(
          name = name,
          filierId = qs__filier.id
        )
        counter = len(Semester.objects.filter(filierId = qs__filier.id))

        qs__filier.count = counter
        qs__filier.save()

        
        messages.success(request, f"{name} Created successfuly")
      else :
        messages.success(request, f"{name} Created Befor ")
    else:
      messages.warning(request, "Your form not submited not post ")
      forms = semesterModelForm()
  context = {
    "form":forms,
  }
  return render(request,f"{backendsemesterListPath}create.html",context)