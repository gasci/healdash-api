#from django.contrib.auth.models import User

from rest_framework import serializers
#from accounts.models import Account


class UserSerializer(serializers.ModelSerializer):
    
    @classmethod
    def get_username(cls, user):
        
        return user.username
