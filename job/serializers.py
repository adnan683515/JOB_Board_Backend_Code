from rest_framework import serializers
from .models import JOB,Company
from place.serializers import BrowseCetagorySerializers,PlaceSerializers,OrganaigationSerializers
class CompanySerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Company
        fields = ['id','company_name','slug']
        
        read_only_fields=['slug']

class job_serializers(serializers.ModelSerializer):
    # Place = serializers.StringRelatedField(many=False)
    # organizationtype = serializers.StringRelatedField(many=False)
    # Browse_cetagory = serializers.StringRelatedField(many=False)
    # Company = serializers.StringRelatedField(many=False)
    Company = CompanySerializers(read_only=True)
    Place = PlaceSerializers(read_only=True)
    Browse_cetagory  = BrowseCetagorySerializers(read_only=True)
    organizationtype = OrganaigationSerializers(read_only=True)
    
    class Meta:
        model = JOB
        fields= ['id','job_title','logo','Company','salary','age_limit','work_station','employment_status','application_deadline','published','education','experience','address','other_benefits','gender','requirments','Place','Browse_cetagory','organizationtype']
        
        
        
        
