from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get-in-touch/', views.get_in_touch, name='get_in_touch'),
]
