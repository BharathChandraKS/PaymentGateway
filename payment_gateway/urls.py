from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views, api_views

router = DefaultRouter()
router.register(r'payment', api_views.PaymentViewSet, basename='Payment')


urlpatterns = [
    path('', LoginView.as_view(), name='login_view'),
    path('logout/', LogoutView.as_view(), name='logout_view'),
    path('home/', views.HomeView.as_view(), name='home_view'),
    path('accounts/register/', views.PGRegistrationView.as_view(), name='registration_view'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/login/', api_views.APILogin.as_view(), name='api_login'),
    path('api/', include((router.urls, 'api'))),
]