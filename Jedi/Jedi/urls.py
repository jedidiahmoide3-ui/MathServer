from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns = [
    path('', views.Calculate_bill, name='Calculate_bill')
    ]