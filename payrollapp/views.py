from django.shortcuts import render
from .forms import PayrollForm

def calculate_payroll(request):
    if request.method == 'POST':
        form = PayrollForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            total_pay = data['rate_of_pay'] * data['hours_worked']
            return render(request, 'payroll/result.html', {'total_pay': total_pay})
    else:
        form = PayrollForm()
    return render(request, 'payroll/form.html', {'form': form})

def landing_page(request):
    return render(request, 'payroll/landing_page.html')
