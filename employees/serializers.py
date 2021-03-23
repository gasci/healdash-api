from rest_framework import serializers


class EmployeeSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    id_number = serializers.CharField(required=False)
