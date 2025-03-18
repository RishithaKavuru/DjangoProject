from rest_framework import serializers
from . models import UserDetails

# class UserDetailsSerializer(serializers.Serializer):
#     username = serializers.CharField() 
#     email = serializers.EmailField()
#     password = serializers.CharField()

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = '__all__'