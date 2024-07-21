from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class RegisterUserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)
    
    def validate(self, attrs):
        
        if User.objects.filter(username=attrs.get('username')).exists():
            raise serializers.ValidationError('Username already taken')
        
        return attrs
    
    def create(self, validated_data):
        
        user = User.objects.create(first_name=validated_data.get('first_name'),
                                last_name=validated_data.get('last_name'),
                                username=validated_data.get('username').lower()                                
                                )
        user.set_password(validated_data.get('password'))
        user.save()
        
        return validated_data
    
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)
    
    def validate(self, data):
        
        if not User.objects.filter(username=data.get('username')).exists():
            raise serializers.ValidationError('account not found')
        
        return data
    
    def get_jwt_token(self, data):
        
        user = authenticate(username=data.get('username'), password=data.get('password'))
        
        if not user:
            return {"message": "Invalid Credentials","data":{}}
        
        refresh = RefreshToken.for_user(user)
        
        return {"message":"login successful","data":{'refresh': str(refresh),
                                'access': str(refresh.access_token)}}