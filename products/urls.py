from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_coffee, name='coffee')
]
