from django.contrib import admin
from django.urls import path, include
from payrollapp.views import landing_page, calculate_payroll

urlpatterns = [
    path('admin/', admin.site.urls),
    path('payroll/', include('payrollapp.urls')),  # Include app-level URLs
    path('', landing_page, name='landing_page'),
     path('calculator/', calculate_payroll, name='calculator_page'),
]
