from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('dogs/<str:pk>/', views.dogs, name = "dogs")
]