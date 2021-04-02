from rest_framework import serializers


class EmployeeSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    role = serializers.CharField(max_length=200, required=False)
    id_number = serializers.CharField(max_length=50, required=False)
