from . import views
from django.urls import path

urlpatterns = [
    path('', views.mostrar, name="home"),
    path('post', views.post, name="post"),
    path('borrar/<int:id>', views.borrar, name="borrar"),
    path('archivar', views.archivar, name="archivar"),
]
