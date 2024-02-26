from django.contrib import admin
from django.urls import path, include
from payrollapp.views import landing_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('payroll/', include('payrollapp.urls')),  # Include app-level URLs
    path('', landing_page, name='landing_page'),
]
