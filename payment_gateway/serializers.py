from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied, NotAuthenticated

from .models import Payment, Company


class PaymentSerializer(serializers.ModelSerializer):
    company = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Payment
        fields = ['id', 'status', 'created_on', 'transacted_on', 'company', 'amount', 'shopper']

    def create(self, validated_data):
        request = self.context["request"]
        creator = request.user
        if not creator.is_authenticated:
            raise NotAuthenticated('Authentication required.')
        company = Company.objects.get(user=creator)
        return Payment.objects.create(company=company, status='CREATED',
                                      shopper=validated_data['shopper'],
                                      amount=validated_data['amount'])

    def update(self, instance, validated_data):
        request = self.context['request']
        creator = request.user
        if not creator.is_authenticated or instance.company.user != creator:
            raise PermissionDenied('Permission denied, you have not created this transaction')
        instance.amount = validated_data['amount']
        instance.shopper = validated_data['shopper']
        instance.save()
        return instance




