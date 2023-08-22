from django.urls import path

from . import views

app_name='app'

urlpatterns = [
    path("", views.index, name="index"),
    path("sobre", views.index, name="sobre"),
    path("equipe", views.index, name="equipe"),
  
  
   
]


