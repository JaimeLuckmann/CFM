from django.urls import path
from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LoginView, logout_then_login, LogoutView
from django.contrib.auth import login
from applications.login.views import *

app_name = "login_app"


urlpatterns = [
    #path('',login,{'template_name':'login/login.html'},name="login"),
    # path('registro/',views.userRegisterView.as_view(),name="registro"),
    path('',views.loginUser.as_view(),name="login"),
    path('logout/',views.LogoutView.as_view(),name="logout"),
    path('registro/',views.register,name="register"),

]

urlpatterns += staticfiles_urlpatterns()