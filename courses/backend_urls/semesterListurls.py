
from django.urls import path
from courses.includes.semesterList import (
  backendSemesetrList,
  semesterCreateViews
)
# app_name = "semesterListurls" 

urlpatterns = [

     # SmesterList :
    path('List/',backendSemesetrList, name = "backend-Semester-List" ),
    # path('categories/', CategoryListView.as_view(), name='category-list'),
    # path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    # path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    # path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    path('Create/', semesterCreateViews, name='backend-Semester-create'),
    ]