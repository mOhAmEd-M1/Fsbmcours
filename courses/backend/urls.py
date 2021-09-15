from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
# from django.conf.urls import  url
from django.views.static import serve
from courses import views
from courses.includes.courseList import *
urlpatterns = [

  
  # path('Eduction/<filier>/module-Detail/',views.ModulePanelPage,name ="modl-panel-page"),
  #  path('<filier>/<semster>/<modl>/delete/',views.Deletemodl,name ="Deletemodl-panel-page"),
  #  path('<filier>/<semster>/create/',views.Createmodl,name ="Createmodl-panel-page"),
  #  path('<filier>/<semster>/<modl>/edit/',views.Editmodl,name ="Editmodl-panel-page"),
]