from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import  url
from django.views.static import serve
from eduction import views


urlpatterns = [
   path('',views.homepage),
   path('<fil>/',views.filier_Page, name='filier-name'),
   path('<fil>/<semester>/',views.semister_Page, name='semister-name'),
   path('<fil>/<semester>/<modl>/',views.modulePage, name='module-Detail'),
]