from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('applications.login.urls')),
    path('',include('applications.home.urls')),
    path('',include('applications.aparato.urls')),
    path('',include('applications.seccion.urls')),
    path('',include('applications.pieza.urls')),
]
