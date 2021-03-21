from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import generics

from .serializers import UserSerializer


class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer


class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
