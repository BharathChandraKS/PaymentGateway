from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.views import APIView

from .models import Payment, Company
from .serializers import PaymentSerializer


class APILogin(APIView):

    def post(self, request):
        user = authenticate(username=request.data.get("username"), password=request.data.get("password"))
        if not user:
            return Response({'error': 'Credentials are incorrect or user does not exist'},
                            status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=HTTP_200_OK)


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = User.objects.get(pk=self.request.user.pk)
        try:
            company = Company.objects.get(user=user)
        except Company.DoesNotExist:
            raise Http404
        payments = Payment.objects.filter(company=company).order_by('-created_on')
        return payments
