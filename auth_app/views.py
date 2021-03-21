from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status

from .serializers import RegisterSerializer, MyTokenObtainPairSerializer


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer


class TokenCheckView(APIView):
    """
    check if the token is valid
    """
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        """
        Return token_valid if token is valid.
        """
        if(request.user.username):
            return Response("valid_token", status=status.HTTP_200_OK)
        else:
            return Response("invalid_token", status=status.HTTP_400_BAD_REQUEST)
