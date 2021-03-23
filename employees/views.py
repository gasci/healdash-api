from rest_framework import permissions
from rest_framework import generics
from rest_framework import authentication

from .serializers import EmployeeSerializer

from .models import Employee
# Create your views here.


class EmployeesListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)
