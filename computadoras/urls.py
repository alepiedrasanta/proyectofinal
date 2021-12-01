from django.urls import path
from .import views

urlpatterns = [
    path('compus/listar', views.compus_lista, name ='compus_lista'),
    path('compus/nueva/', views.compus_nueva, name='compus_nueva'),
    path('compus/<int:pk>/editar/', views.compus_editar, name ='compus_editar'),
    path('compus/<int:pk>', views.compus_detalle, name ='compus_detalle'),
    path('compus/<pk>/borrar/', views.compus_borrar, name ='compus_borrar'),
    path('', views.menu, name ='menu'),
  ]