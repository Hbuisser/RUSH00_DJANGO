from django.urls import path
from . import views

urlpatterns = [
    path('', views.title_page, name='base'),
    path('moviemon/', views.begin),
    path('battle/<str:id>', views.battle)
    # path('battle/', views.battle,  name='base')
]
# <str:id>