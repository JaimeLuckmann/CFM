from django.urls import path
from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "pieza_app"

urlpatterns = [
    path('pieza', views.pieza ,name="pieza")
]

urlpatterns += staticfiles_urlpatterns()