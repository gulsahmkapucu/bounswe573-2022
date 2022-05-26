"""learnwithus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('',views.index, name="index"),
    path('courses',views.list_page, name="courses"),
    # path('coursedetail/<int:cid>',views.detail_page, name="coursedetail"),
    path('accounts/register', views.RegisterPage.as_view(template_name="accounts/register.html"), name='accounts/register'),
    path("accounts/profile", views.ProfileView.as_view(), name="profile"),
    path('searchbar/',views.SearchView.as_view(), name='searchbar'),
    path('',views.PostIndexView.as_view(),name='post-list'),    
    path('coursedetail/<int:pk>',views.CourseDetail.as_view(), name="coursedetail"),



#Django Auth
path('accounts/login',auth_views.LoginView.as_view(template_name="accounts/login.html"), name="accounts/login"),
path("accounts/logout", auth_views.LogoutView.as_view(),name="logout"),

]
