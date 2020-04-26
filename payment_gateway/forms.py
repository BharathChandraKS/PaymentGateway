from django import forms
from django_registration.forms import RegistrationForm


class PGRegistrationForm(RegistrationForm):
    company_name = forms.CharField(label='Company Name', max_length=100)
    account_number = forms.CharField(label='Account Number', max_length=12)
    bsb = forms.CharField(label='BSB', max_length=6)
