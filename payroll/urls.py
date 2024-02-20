from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('payroll/', include('payrollapp.urls')),  # Include app-level URLs
]
