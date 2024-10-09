
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import register_model


class user_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email']
        

class RegistrationSerializers(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    country = serializers.CharField(required=True)
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','confirm_password','country']
    
    
    def save(self):
        username= self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password1 = self.validated_data['password']
        password2 = self.validated_data['confirm_password']
        country = self.validated_data['country']
        
        
        if password1 != password2:
            raise serializers.ValidationError({'error':"Password doesn't match"})
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error':"This email already exit"})
        
        user = User(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
        # account = UserCountry(country=country,user=user)
        user.set_password(password1)
        user.is_active = False
        user.save()

        
        
        register_model.objects.create(
            user=user,
            country=country
            
        )
        
        
        
       
        return user
    
    
class loginSerializers(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    
    
class passwordChangeSerilizer(serializers.Serializer):
    model = User
    
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)
    

