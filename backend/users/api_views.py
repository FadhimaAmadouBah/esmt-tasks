from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import CustomUser
from .serializers import UserSerializer, RegisterSerializer


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class MeAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()