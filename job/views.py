from django.shortcuts import render
from rest_framework import viewsets
from .models import JOB,Company
from .serializers import job_serializers,CompanySerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework import pagination
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class JOBtList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        all_job =JOB.objects.all()
        serializer = job_serializers(JOB, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = job_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.

class pageinationView(pagination.PageNumberPagination):
    page_size = 4 #item per size
    page_size_query_param = 'page_size'
    max_page_size = 1000
0
class job_Viewset(viewsets.ModelViewSet):
    queryset = JOB.objects.all()
    serializer_class = job_serializers
    
    # permission_classes = [IsAuthenticated]
    # pagination_class = pageinationView
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        
        company_id = self.request.query_params.get('Company_id')
        if company_id:
            queryset = queryset.filter(Company_id = company_id)
        
        place_id = self.request.query_params.get('Place_id')
        if place_id:
            queryset = queryset.filter(Place_id = place_id)
            
        Browse_cetagory_id = self.request.query_params.get('Browse_cetagory_id')
        
        if Browse_cetagory_id :
            queryset = queryset.filter(Browse_cetagory_id = Browse_cetagory_id)
        
        organizationtype_id = self.request.query_params.get('organizationtype_id')
        
        if organizationtype_id:
            queryset = queryset.filter(organizationtype_id = organizationtype_id)
            
        return queryset    
        
        
    
    
    
    


class companyViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    
    queryset = Company.objects.all()
    serializer_class = CompanySerializers