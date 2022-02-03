from django.urls import path
from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "seccion_app"

urlpatterns = [
    path('seccion',views.seccion,name="seccion"),
]

urlpatterns += staticfiles_urlpatterns()