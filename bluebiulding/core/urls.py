from django.contrib import admin
from django.urls import path
from bluebiulding.core import views

app_name="core"

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
]