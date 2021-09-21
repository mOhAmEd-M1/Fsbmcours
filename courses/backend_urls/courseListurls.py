from django.urls import path
from courses.includes.courseList import (
  backendCoursesList,
  CoursesCreateViews,
)

app_name = "courseListurls" 

urlpatterns = [
  
     # coursesList :
    path('List/<int:moduleID>/',backendCoursesList, name = "backend-courses-List" ),
    # path('categories/', CategoryListView.as_view(), name='category-list'),
    # path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    # path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    # path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    # path('AdminPanel/courses/<int:semesterid>/module-create/', moduleCreateViews, name='backend-module-create'),
    path('Create/<int:moduleID>/', CoursesCreateViews, name='backend-courses-create'),
]