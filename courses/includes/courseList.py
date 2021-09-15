from django import forms
from django.forms.models import ModelForm
from django.shortcuts import redirect, render,get_object_or_404
from courses.models import *
from django.http import Http404
from django.core.files.storage import FileSystemStorage
import datetime
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.http import HttpResponseRedirect ,JsonResponse
import os
from django.contrib.auth.decorators import login_required





re__path_backend = "backend/courses/courseList"
re__path = "frontend/courses"

def course_list(request,filier,semester,modl):
  try:
    fil__qs = Filier.objects.get(name = filier)
    sem__qs = Semester.objects.get(filierId = fil__qs.id, slug = semester)
    modl__qs = Module.objects.get(filierid = fil__qs.id,semmesterid = sem__qs.id,slug = modl)
  except :
    raise Http404()
  context = {
    "fileNumber": modl__qs.ccount + modl__qs.Tdcount + modl__qs.tpcount +modl__qs.ecount,
     # query Header
    "Filires":Filier.objects.all(),
    # end 
    "semester":Semester.objects.filter(filierId = fil__qs.id ,slug = sem__qs.slug),
    "Modules":Module.objects.filter(filierid = fil__qs.id,semmesterid = sem__qs.id,slug = modl),
    'Courses':Courses.objects.filter(filierid= fil__qs.id ,semesterid= sem__qs.id ,moduleid = modl__qs.id )

  }
  return render(request,f'{re__path}/courseList.html',context)
# backend functions

backendcoursesListPath = "backend/courses/coursesList/"
from courses.mixins import OrganisorAndLoginRequiredMixin
from courses.forms import CoursesModelFormviews
from django.contrib import messages
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin



def backendCoursesList(request,moduleID):

  module_qs = Module.objects.get(id = moduleID )
  semester_qs = Semester.objects.get(id = module_qs.semmesterid)
  filier_qs = Filier.objects.get(id = semester_qs.filierId)

  context = {
    "module_qs":module_qs,
    "filier_qs":filier_qs,
    "semester_qs" : semester_qs,
    "Filires":Filier.objects.all(),
    "semester":Semester.objects.filter(id = module_qs.semmesterid),
    "Modules":Module.objects.filter(id = moduleID),
    "Courses":Courses.objects.filter(moduleid =module_qs.id )
  }
  return render(request,f'{backendcoursesListPath}list.html',context)


# class CoursesCreateViews(OrganisorAndLoginRequiredMixin, generic.CreateView):

#     template_name = f"{backendcoursesListPath}create.html"
#     form_class = coursesModelForm

#     def get_success_url(self, *args, **kwargs):
#         return reverse("backend-courses-create", args=[int(self.kwargs['moduleID'])])

#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         # Add in a QuerySet of all the books
#         QuerySet_modl = Module.objects.get(id =self.kwargs['moduleID'] )
#         QuerySet = Semester.objects.get(id =QuerySet_modl.semmesterid )

#         context['Module_list'] = QuerySet_modl
#         context['Semester_list'] = QuerySet
#         context['Filier_list'] = Filier.objects.get(id =QuerySet.filierId)
#         return context

#     def form_valid(self, form , *args, **kwargs):
#       try:
#         print("Oki")
        
#         module_qs = Module.objects.get(id = int(self.kwargs['moduleID']))
#         semester_qs = Semester.objects.get(id = module_qs.semesterid)
#         filier_qs = Filier.objects.get(id = semester_qs.filierId )
#         print(f"________________{module_qs.name}")
#         name = form.cleaned_data['name']
#         courses_type = form.cleaned_data['C_type']

#         if len(Courses.objects.filter(name = name,semmesterid=semester_qs.id,filierid=filier_qs.id)) != 0 :
#           messages.warning(self.request, f"{name} Created Befor ")
#         else:
#           category = form.save(commit=False)

#           form.instance.moduleid = self.kwargs['moduleID']
#           form.instance.semesterid = semester_qs.id
#           form.instance.filierid = filier_qs.id

#           # category.organisation = self.request.user.userprofile

#           category.save()
#           get__counter = module_qs

#           if courses_type == "cours":
#             counter = len(Courses.objects.filter(C_type="cours",moduleid=self.kwargs['moduleID'] ,semesterid=semester_qs.id,filierid=filier_qs.id))
#             get__counter.ccount = counter

#           elif courses_type == "Traveaux derigie":
#             counter = len(Courses.objects.filter(C_type="Traveaux derigie",moduleid=self.kwargs['moduleIDmoduleID'] ,semesterid=semester_qs.id,filierid=filier_qs.id))
#             get__counter.Tdcount = counter

#           elif courses_type == "Traveaux pratique":
#             counter = len(Courses.objects.filter(C_type ="Traveaux pratique",moduleid=self.kwargs['moduleIDmoduleID'] ,semesterid=semester_qs.id,filierid=filier_qs.id))
#             get__counter.tpcount = counter
          
#           elif courses_type == "exam":
#             counter = len(Courses.objects.filter(C_type="exam",moduleid=self.kwargs['moduleID'] ,semesterid=semester_qs.id,filierid=filier_qs.id))
#             get__counter.ecount = counter

#           get__counter.save()
#           messages.success(self.request, f" {name} Created successfuly")
#       except:
#           messages.success(self.request, "problen")

#       return super(CoursesCreateViews, self).form_valid(form)

def CoursesCreateViews(request,moduleID):
    module_qs = Module.objects.get(id = moduleID)
    semester_qs = Semester.objects.get(id = module_qs.semmesterid)
    filier_qs = Filier.objects.get(id = semester_qs.filierId )
    form = CoursesModelFormviews()
    if request.method == "POST":
        form = CoursesModelFormviews(request.POST or None,request.FILES or None)
        if form.is_valid():
          name = form.cleaned_data['name']
          courses_type = form.cleaned_data['C_type']
          if len(Courses.objects.filter(name = name,semesterid=semester_qs.id,filierid=filier_qs.id)) != 0 :
            messages.warning(request, f"{name} Created Befor ")
          else:
            form.instance.moduleid = module_qs.id
            form.instance.semesterid = semester_qs.id
            form.instance.filierid = filier_qs.id

            form.save()

            get__counter = module_qs

            if courses_type == "cours":

              counter = len(Courses.objects.filter(C_type="cours",moduleid=moduleID,semesterid=semester_qs.id,filierid=filier_qs.id))
              get__counter.ccount = counter

            elif courses_type == "Traveaux derigie":

              counter = len(Courses.objects.filter(C_type="Traveaux derigie",moduleid=moduleID,semesterid=semester_qs.id,filierid=filier_qs.id))
              get__counter.Tdcount = counter

            elif courses_type == "Traveaux pratique":

              counter = len(Courses.objects.filter(C_type ="Traveaux pratique",moduleid=moduleID,semesterid=semester_qs.id,filierid=filier_qs.id))
              get__counter.tpcount = counter
            
            elif courses_type == "exam":

              counter = len(Courses.objects.filter(C_type="exam",moduleid=moduleID ,semesterid=semester_qs.id,filierid=filier_qs.id))
              get__counter.ecount = counter

            get__counter.save()
            messages.success(request, f" {name} Created successfuly")
        else:
          messages.warning(request, "From is not valid")
        return redirect("backend-courses-create",moduleID)
    context = {
        "form": form,
        "Module_list":module_qs,
        "Semester_list":semester_qs,
        "Filier_list":filier_qs,
    }
    return render(request, f"{backendcoursesListPath}create.html", context)

