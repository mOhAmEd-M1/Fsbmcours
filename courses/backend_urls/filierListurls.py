from django.urls import path
from courses.views import (
  backendFilierList,
  CategoryCreateView
)
# app_name = "filierListurls" 

urlpatterns = [
  
    # filierList :
    path('List/',backendFilierList, name = "backend-Filier-List" ),
    # path('categories/', CategoryListView.as_view(), name='category-list'),
    # path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    # path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    # path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    path('Create/', CategoryCreateView.as_view(), name='backend-Filier-create'),
    
    ]