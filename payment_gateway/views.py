from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View
from django_registration.backends.one_step.views import RegistrationView

from .forms import PGRegistrationForm
from .models import BankAccount, Company
from django_registration import signals

User = get_user_model()


class PGRegistrationView(RegistrationView):
    form_class = PGRegistrationForm

    def register(self, form):
        new_user = form.save()
        bank_account = BankAccount.objects.create(account=form.cleaned_data['account_number'],
                                                  bsb=form.cleaned_data['bsb'])
        Company.objects.create(user=new_user, payment_details=bank_account,
                               company_name=form.cleaned_data['company_name'])
        new_user = authenticate(
            **{
                User.USERNAME_FIELD: new_user.get_username(),
                "password": form.cleaned_data["password1"],
            }
        )
        login(self.request, new_user)
        signals.user_registered.send(
            sender=self.__class__, user=new_user, request=self.request
        )
        return new_user

    def get_success_url(self, user=None):
        return reverse('home_view')


class HomeView(LoginRequiredMixin, View):
    template_name = 'home_page.html'

    def get(self, request, *args, **kwargs):
        company = Company.objects.get(user=request.user)
        return render(request, self.template_name, {'company': company.company_name,
                                                    'user': company.user.username,
                                                    'email': company.user.email,
                                                    'account_number': company.payment_details.account,
                                                    'bsb': company.payment_details.bsb})


