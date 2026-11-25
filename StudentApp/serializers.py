from rest_framework import serializers
from StudentApp.models import Student
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id','username', 'email','password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'



