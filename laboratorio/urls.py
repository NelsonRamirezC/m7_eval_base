from django.urls import path

from . import views

urlpatterns = [
    path('laboratorios/', views.laboratorios, name="laboratorios"),
]
