import courses
from django.shortcuts import render , redirect
from .models import *
from django.http import Http404
# Create your views here.
from django.views import generic
from .forms import (
    CustomUserCreationForm,
    CategoryModelForm,
)
class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")


def index(request):
  context = {
    "Filires":Filier.objects.all(),
    "Courses":Courses.objects.all(),
  }
  return render(request,'frontend/courses/index.html',context)

def indexBackend(request):
  context = {
     "Filires":Filier.objects.all(),
    "Courses":Courses.objects.all(),
  }
  return render(request,"backend/courses/landing.html",context)


backendFilierListPath = "backend/courses/filierList/"
from .mixins import OrganisorAndLoginRequiredMixin
from django.contrib import messages

def backendFilierList(request):
  if not request.user.is_superuser:
      messages.warning(request, f"{request.user.username} You Are Not Admin ")
      return redirect("backendIndex")
  context = {
    "Filires":Filier.objects.all(),
  }
  return render(request,f"{backendFilierListPath}index.html",context)


class CategoryCreateView(OrganisorAndLoginRequiredMixin, generic.CreateView):
    template_name = f"{backendFilierListPath}create.html"
    form_class = CategoryModelForm

    def get_success_url(self):
        return reverse("backend-Filier-List")

    def form_valid(self, form):
        category = form.save(commit=False)
        # category.organisation = self.request.user.userprofile
        category.save()
        return super(CategoryCreateView, self).form_valid(form)
