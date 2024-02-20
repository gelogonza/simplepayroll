from django.urls import path
from .views import calculate_payroll

urlpatterns = [
    path('calculate/', calculate_payroll, name='calculate_payroll'),
]
