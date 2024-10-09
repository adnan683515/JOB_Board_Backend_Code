from django.shortcuts import render
from rest_framework import viewsets
from .models import Place,Browse_cetagory,organizationtype,work_type
from .serializers import BrowseCetagorySerializers,PlaceSerializers,OrganaigationSerializers,WorkSerializers
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class WorkViewSet(viewsets.ModelViewSet):
    
    # permission_classes = [IsAuthenticated]
    
    queryset = work_type.objects.all()
    serializer_class = WorkSerializers


class BrowseViewSet(viewsets.ModelViewSet):
    
    # permission_classes = [IsAuthenticated]
    
    queryset = Browse_cetagory.objects.all()
    serializer_class = BrowseCetagorySerializers


class PlaceViewSet(viewsets.ModelViewSet):
    
    # permission_classes  = [IsAuthenticated]
    
    queryset = Place.objects.all()
    serializer_class = PlaceSerializers


class OrganaigationViewSet(viewsets.ModelViewSet):
    
    # permission_classes  = [IsAuthenticated]
    
    queryset = organizationtype.objects.all()
    serializer_class = OrganaigationSerializers


