from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from courses.models import *
from django.http import Http404

re__path = "frontend/courses/"

def module_list(request,filier,semester):
  try:
    fil__qs = Filier.objects.get(name = filier)
    sem__qs = Semester.objects.get(filierId = fil__qs.id, slug = semester)
    shoow = sem__qs
    shoow.show = shoow.show + 1
    shoow.save()
    print(f"shoow : {sem__qs.show}")
  except :
    return Http404()
  context = {
    # query Header
    "Filires":Filier.objects.all(),
    # end 
    "semestre":sem__qs,
    "filire":fil__qs,
    "semester":Semester.objects.filter(filierId = fil__qs.id ,slug = sem__qs.slug),
    "Modules":Module.objects.filter(filierid = fil__qs.id,semmesterid = sem__qs.id),
    "Courses":Courses.objects.filter(filierid = fil__qs.id,semesterid = sem__qs.id),


  }
  return render(request,f'{re__path}/moduleList.html',context)

backendmoduleListPath = "backend/courses/modulesList/"
from courses.mixins import OrganisorAndLoginRequiredMixin
from courses.forms import moduleModelForm
from django.contrib import messages
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin



def backendmoduleList(request,semesterid):
  if not request.user.is_superuser:
    messages.warning(request, f"{request.user.username} You Are Not Admin ")
    return redirect("backendIndex")
  semester_qs = Semester.objects.get(id = semesterid)
  filier_qs = Filier.objects.get(id = semester_qs.filierId)
  context = {
    "filier_qs":filier_qs,
    "semester_qs" : semester_qs,
    "Filires":Filier.objects.all(),
    "semester":Semester.objects.filter(id = semesterid),
    "Modules":Module.objects.filter(semmesterid = semesterid),
  }
  return render(request,f'{backendmoduleListPath}list.html',context)


class moduleCreateViews(OrganisorAndLoginRequiredMixin, generic.CreateView):
    template_name = f"{backendmoduleListPath}create.html"
    form_class = moduleModelForm

    def get_success_url(self, *args, **kwargs):
        return reverse("moduleListurls:backend-module-create", args=[int(self.kwargs['semesterid'])])

    def form_valid(self, form , *args, **kwargs):

        semester_qs = Semester.objects.get(id = int(self.kwargs['semesterid']))
        print("oki 1")
        print(f'____semesterID = {semester_qs.name}')
        filier_qs = Filier.objects.get(id = semester_qs.filierId )
        print("oki 2")
        print(f'____filierID = {filier_qs.name}')

        name = form.cleaned_data['name']
        if len(Module.objects.filter(name = name,semmesterid=semester_qs.id,filierid=filier_qs.id)) != 0 :
          messages.warning(self.request, f"{name} Created Befor ")
        else:
          category = form.save(commit=False)
          form.instance.semmesterid = self.kwargs['semesterid']
          form.instance.filierid = filier_qs.id
          # category.organisation = self.request.user.userprofile
          

          category.save()
          counter = len(Module.objects.filter(semmesterid=semester_qs.id, filierid=filier_qs.id))
          print(f"counter ___ {counter}   ")
          get__counter = semester_qs
          get__counter.count = counter
          get__counter.save()
          messages.success(self.request, f" {name} Created successfuly")

        return super(moduleCreateViews, self).form_valid(form)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        QuerySet = Semester.objects.get(id =self.kwargs['semesterid'] )
        context['Semester_list'] = QuerySet
        context['Filier_list'] = Filier.objects.get(id =QuerySet.filierId)
        return context
