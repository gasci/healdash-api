from rest_framework.views import APIView
from rest_framework import permissions, authentication
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .serializers import EmployeeSerializer
from .models import Employee

from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.


class EmployeesListView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = Employee.objects.all()
        
        paginator = PageNumberPagination()
        paginator.page_size = 3

        objs = paginator.paginate_queryset(queryset, request)
        serializer = EmployeeSerializer(objs, many=True)

        return paginator.get_paginated_response(serializer.data)



