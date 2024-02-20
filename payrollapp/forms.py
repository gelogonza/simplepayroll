from django import forms
from .models import PayrollEntry

class PayrollForm(forms.ModelForm):
    class Meta:
        model = PayrollEntry
        fields = ['name', 'rate_of_pay', 'hours_worked']
