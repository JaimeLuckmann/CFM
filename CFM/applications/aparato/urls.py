from django.urls import path
from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('aparato',views.aparato),
]

urlpatterns += staticfiles_urlpatterns()