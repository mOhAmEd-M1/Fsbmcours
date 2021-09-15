from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import  url
from django.views.static import serve
from courses import views
from django.contrib.auth.views import (
    LoginView, 
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from courses.views import SignupView
from courses.views import (
    CategoryCreateView,
    semesterCreateViews,
    )
from courses.includes.moduleList import (
    moduleCreateViews,
)
from courses.includes.courseList import (
    CoursesCreateViews,
    # backendCoursesList,
)
urlpatterns = [
    url(r'^Media/(?P<path>.*)$',serve , {'document_root':settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$',serve , {'document_root':settings.STATIC_ROOT}),
   
    path('admin/', admin.site.urls),
    path('signup/', SignupView.as_view(), name='signup'),
    path('reset-password/', PasswordResetView.as_view(), name='reset-password'),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # ---Courses Urls----
    # _FrontEnd's Urls: --

    path("",views.index,name="index__page"),

    path('courses/filier-Detail/',views.filier_list, name='front-filier-list'),
    path('courses/<filier>/',views.semester_list, name='front-semester-list'),
    path('courses/<filier>/<semester>/',views.module_list, name='front-module-list'),
    path('courses/<filier>/<semester>/<modl>/',views.course_list, name='front-course-list'),
    # _BackEnd's Urls: 

    path('AdminPanel/', views.indexBackend , name = "backendIndex"),
    # filierList :
    path('AdminPanel/courses/filier-List/',views.backendFilierList, name = "backend-Filier-List" ),
    # path('categories/', CategoryListView.as_view(), name='category-list'),
    # path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    # path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    # path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    path('AdminPanel/courses/filier-create/', CategoryCreateView.as_view(), name='backend-Filier-create'),
    
     # SmesterList :
    path('AdminPanel/courses/Semester-List/',views.backendSemesetrList, name = "backend-Semester-List" ),
    # path('categories/', CategoryListView.as_view(), name='category-list'),
    # path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    # path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    # path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    path('AdminPanel/courses/Semester-create/', views.semesterCreateViews, name='backend-Semester-create'),
    
     # moduleList :
    path('AdminPanel/courses/<int:semesterid>/module-List/',views.backendmoduleList, name = "backend-module-List" ),
    # path('categories/', CategoryListView.as_view(), name='category-list'),
    # path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    # path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    # path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    # path('AdminPanel/courses/<int:semesterid>/module-create/', views.moduleCreateViews, name='backend-module-create'),
    path('AdminPanel/courses/<int:semesterid>/module-create/', moduleCreateViews.as_view(), name='backend-module-create'),
    

     # coursesList :
    path('AdminPanel/courses/<int:moduleID>/courses-List/',views.backendCoursesList, name = "backend-courses-List" ),
    # path('categories/', CategoryListView.as_view(), name='category-list'),
    # path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    # path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    # path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    # path('AdminPanel/courses/<int:semesterid>/module-create/', views.moduleCreateViews, name='backend-module-create'),
    path('AdminPanel/courses/<int:moduleID>/courses-create/', views.CoursesCreateViews, name='backend-courses-create'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
