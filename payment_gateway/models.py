from django.contrib.auth.models import User
from django.db import models


class BankAccount(models.Model):
    account = models.CharField(max_length=50)
    bsb = models.CharField(max_length=10)

    def __str__(self):
        return self.account


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200, help_text="Name of the company")
    payment_details = models.ForeignKey(BankAccount, on_delete=models.CASCADE)

    def __str__(self):
        return self.company_name


class Payment(models.Model):
    PAYMENT_CHOICES = [
        ('CREATED', 'created'),
        ('SUCCESSFUL', 'successful'),
        ('FAILED', 'failed'),
        ('DISPUTED', 'disputed')
    ]
    status = models.CharField(max_length=20, help_text="Payment status", choices=PAYMENT_CHOICES, default='created')
    created_on = models.DateTimeField(auto_now_add=True, help_text="Time of creation")
    transacted_on = models.DateTimeField(auto_now=True, help_text="Time of transaction")
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    shopper = models.CharField(max_length=100, help_text='User who initiated the transaction')
    amount = models.FloatField(help_text='Transaction amount')

    def __str__(self):
        return self.company.company_name

