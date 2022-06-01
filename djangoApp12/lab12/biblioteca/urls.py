from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^prestamos/$', views.JSONResponse.prestamo_list),
    re_path(r'^prestamos/(?P<pk>[0-9]+)/$', views.JSONResponse.prestamo_detail),
]