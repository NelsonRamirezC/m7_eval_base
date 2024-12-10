from django.urls import path

from . import views

urlpatterns = [
    path('', views.fotografias, name="fotografias"),
     path('compartir/<int:fotografia_id>/', views.compartir_fotografia, name="compartir_fotografia"),
     path('compartir/remove/<int:fotografia_id>/<int:usuario_id>/', views.deja_compartir_fotografia, name="deja_compartir_fotografia"),
]
