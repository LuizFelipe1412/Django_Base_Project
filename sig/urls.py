from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_sig, name='home_sig')
]