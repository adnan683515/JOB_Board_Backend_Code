from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ContactSerializers,OurLeaderSerializers
from .models import contact_Model,our_leaders
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
# Create your views here.
class LargeResultsSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000

class ContactViewSet(viewsets.ModelViewSet):
    permission_classes  = [IsAuthenticated]
    
    
    queryset= contact_Model.objects.all()
    serializer_class = ContactSerializers
    
    
class OurLeaderViewSet(viewsets.ModelViewSet):
    # permission_classes  = [IsAuthenticated]
    
    
    
    queryset = our_leaders.objects.all()
    serializer_class = OurLeaderSerializers
    
    # pagination_class = LargeResultsSetPagination
   
    