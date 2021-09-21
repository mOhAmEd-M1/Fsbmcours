from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import  url
from django.views.static import serve
from courses.views import (
    indexBackend,
    index,
)
from django.contrib.auth.views import (
    LoginView, 
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from courses.views import SignupView

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

    path('courses/',  include('courses.urls')),
    path('dashboard/filier/',  include('courses.backend_urls.filierListurls')),#, namespace="filierListurls"
    path('dashboard/semester/',  include('courses.backend_urls.semesterListurls')),#, namespace="semesterListurls"
    path('dashboard/module/',  include('courses.backend_urls.moduleListurls', namespace="moduleListurls")),#
    path('dashboard/course/',  include('courses.backend_urls.courseListurls', namespace="courseListurls")),#

    # ---Courses Urls----
    # _FrontEnd's Urls: --

    path("",index,name="index__page"),

       # _BackEnd's Urls: 
    path('dashboard/', indexBackend , name = "backendIndex"),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
