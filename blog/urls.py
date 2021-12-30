from django.urls import path
from . import views

app_name='blog'

urlpatterns = [
    path('', views.home, name='home'),
    path("all_post/", views.all_post, name="all_post"),
    path('details/<str:slug>/', views.details, name='details'),
]


