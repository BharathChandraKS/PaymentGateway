from django.contrib import admin
from django.contrib.auth.models import Group

from .models import BankAccount, Company, Payment


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'payment_details')


admin.site.unregister(Group)
admin.site.register(BankAccount)
admin.site.register(Company)
admin.site.register(Payment)