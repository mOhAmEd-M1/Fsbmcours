from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import  url
from django.views.static import serve
from panel import views


urlpatterns = [
   path('',views.homepanel,name="panel"),
   path('<filier>/',views.FilierPanelPage,name="filier-panel-page"),
]