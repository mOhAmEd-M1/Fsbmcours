from django.urls import path
from courses.includes.moduleList import (
  backendmoduleList,
  moduleCreateViews
)
app_name = "moduleListurls" 

urlpatterns = [
 
     # moduleList :
    path('List/<int:semesterid>/',backendmoduleList, name = "backend-module-List" ),
    # path('categories/', CategoryListView.as_view(), name='category-list'),
    # path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    # path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    # path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),

    path('Create/<int:semesterid>/', moduleCreateViews.as_view(), name='backend-module-create'),
    ]