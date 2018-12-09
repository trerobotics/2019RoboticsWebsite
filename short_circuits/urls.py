from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register', views.register, name='register'),
    path('team_info/', views.team_info, name='team_info')
]