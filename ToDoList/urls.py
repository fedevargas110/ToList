from . import views
from django.urls import path

urlpatterns = [
    path('', views.mostrar, name="home"),
    path('post', views.post, name="post"),
]
