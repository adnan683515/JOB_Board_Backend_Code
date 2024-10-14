from django.shortcuts import render,redirect
from rest_framework.views import APIView
from .serializers import RegistrationSerializers,loginSerializers,passwordChangeSerilizer,user_serializer
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth import logout,logout
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from rest_framework import status
from . models import register_model
from rest_framework import status
from django.http import Http404
# Create your views here.

class user_view (APIView):
    
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
                
    def get(self, request, pk, format=None):
        usr = self.get_object(pk)
        serializer = user_serializer(usr)
        return Response(serializer.data)
    

    def put(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer =user_serializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    

        
    
    
class RegisterViewSet(APIView):
    serializer_class = RegistrationSerializers
    



    def post(self,request,format=None):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            
            token = default_token_generator.make_token(user)
            
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            
            confirm_link = f"http://127.0.0.1:8000/active/{uid}/{token}/"
            
            
            email_subject = "confirmation Email"
            
            email_body = render_to_string('email.html',{'confirm_email':confirm_link,'email_subject':email_subject})
            email = EmailMultiAlternatives(email_subject," ",to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            
            return Response('Check your email please!')
        
        return Response(serializer.errors)
    
    
    
class info_user_for_pk(APIView):
    
    def get_object(self, pk):
        try:
            return register_model.objects.get(pk=pk)
        except register_model.DoesNotExist:
            raise Http404

            
    def get(self, request, pk, format=None):
        usr = self.get_object(pk)
        serializer = RegistrationSerializers(usr)
        return Response(serializer.data)
    
    

    
class LoginViews(APIView):
    
    def post(self,request):
        serializer = loginSerializers(data=self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username,password=password)
            if user:
                token,_ = Token.objects.get_or_create(user=user)
            
                login(request,user)
                return Response({'token':token.key,'user_id':user.pk},status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors)
        
        
        
        
def activate(request,uidb64,token):
    
    try :
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(user.DoesNotExist):
        user = None
    
    
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active = True
        
        user.save()
        return redirect('http://127.0.0.1:5500/html/login.html')
    
    else:
        return redirect('http://127.0.0.1:5500/html/register.html')
    
    
    
class logoutView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        request.user.auth_token.delete()
        logout(request)
        return redirect('login')
    
    
class changePasswordView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_object(self,queryset=None):
        return self.request.user
    
    def put(self,request,*args, **kwargs):
        self.object = self.get_object()
        serializer = passwordChangeSerilizer(data=request.data)
        
        if serializer.is_valid():
            pass1 = serializer.data.get('new_password')
            pass2 = serializer.data.get('confirm_password')
            
            if pass1 != pass2:
                return Response("Password Doesn't Match")
            else:
                self.object.set_password(serializer.data.get('new_password'))
                self.object.save()
                return Response("Password Changed")
        
        return Response(serializer.errors)


