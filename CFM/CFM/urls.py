from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('applications.login.urls')),
    path('',include('applications.home.urls')),
    path('',include('applications.aparato.urls')),
    path('',include('applications.seccion.urls')),
    path('',include('applications.pieza.urls')),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="login/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="login/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="login/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="login/password_reset_done.html"), name="password_reset_complete"),
]
