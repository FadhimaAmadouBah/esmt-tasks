from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .api_views import RegisterAPIView, MeAPIView, UserListAPIView

urlpatterns = [
    path('auth/register/', RegisterAPIView.as_view(), name='api_register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='api_login'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='api_refresh'),
    path('users/me/', MeAPIView.as_view(), name='api_me'),
    path('users/', UserListAPIView.as_view(), name='api_users'),
]