from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import  url
from django.views.static import serve
from panel import views


urlpatterns = [
   path('',views.homepanel,name ="panel"),
   path('Eduction/',views.filierpnelPage,name ="filierpnelPage"),
   
   path('<filier>/',views.FilierPanelPage,name ="filier-panel-page"),
   path('<filier>/delete/',views.DeleteFilier, name ="DeleteFilier-panel-page"),
   path('create/',views.CreateFilier, name ="CreateFilier-panel-page"),
   path('<filier>/edit/',views.EditFilier, name ="EditFilier-panel-page"),

   path('Eduction/Semester-Detail/',views.SemesterPanelPage,name ="semster-panel-page"),
   path('<filier>/<semster>/delete/',views.DeleteSemester,name ="DeleteSemester-panel-page"),
   path('<filier>/create/',views.CreateSemester,name ="CreateSemester-panel-page"),
   path('<filier>/<semster>/edit/',views.EditSemester,name ="EditSemester-panel-page"),

   path('<filier>/<semster>/<modl>/',views.ModulePanelPage,name ="modl-panel-page"),
   path('<filier>/<semster>/<modl>/delete/',views.Deletemodl,name ="Deletemodl-panel-page"),
   path('<filier>/<semster>/create/',views.Createmodl,name ="Createmodl-panel-page"),
   path('<filier>/<semster>/<modl>/edit/',views.Editmodl,name ="Editmodl-panel-page"),
]