from django.urls import path
from . import views

urlpatterns = [
    path('', views.begin, name='base'),
    path('moviemon', views.begin, name='base')
]