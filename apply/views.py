from django.shortcuts import render
from .serializers import ApplySerializers
from rest_framework import viewsets
from .models import Apply
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.template.loader import render_to_string
from django.core.mail import  EmailMultiAlternatives
from auth_app.models import register_model
from rest_framework import status
from django.http import Http404
from auth_app.serializers import RegistrationSerializers

    

class ApplyViewSet(viewsets.ModelViewSet):
    # permission_classes =[IsAuthenticated]
    queryset = Apply.objects.all()
    serializer_class = ApplySerializers

    def get_queryset(self):
        queryset =  super().get_queryset()
        
        job_id = self.request.query_params.get('job_id')
        if job_id:
            queryset=Apply.objects.filter(job_id = job_id)
            
        user_id = self.request.query_params.get('user_id')
        if user_id:
            queryset = Apply.objects.filter(user_id = user_id)
        
        return queryset
    
    
    



######################
from rest_framework import generics
from .serializers import appy_serializer_new

class ApplyCreateView(generics.CreateAPIView):
    queryset = Apply.objects.all()
    serializer_class = appy_serializer_new 
    

        
        
class Edit_for_status_view(APIView):
    
    
    def get_object(self, pk):
        try:
            return Apply.objects.get(pk=pk)
        except Apply.DoesNotExist:
            raise Http404
        
        
    def get(self, request, pk, format=None):
        apply = self.get_object(pk)
        serializer = ApplySerializers(apply)
        return Response(serializer.data)
    

    def put(self, request, pk, format=None):
        apply = self.get_object(pk)
        serializer = ApplySerializers(apply, data=request.data)
        if serializer.is_valid():
            serializer.save()
            mail_sub = 'Congress! Your Are Selected In This Job!'
            email_body = render_to_string('accepted_email.html',{"User_Apply_obj": apply})
            email = EmailMultiAlternatives(mail_sub,'',to=[apply.user.email])
            email.attach_alternative(email_body,'text/html')
            email.send()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
 
class delete_view_apply(APIView):
    
    def get_object(self, pk):
        try:
            return Apply.objects.get(pk=pk)
        except Apply.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        apply = self.get_object(pk)
        serializer = ApplySerializers(apply, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request,pk,format=None):
        apply = self.get_object(pk)
        serializer = ApplySerializers(apply)
        return Response(serializer.data)
    
    def delete(self,request,pk,format=None):
        obj = self.get_object(pk)
        obj.delete()
        return Response("Delete done")