from rest_framework import serializers
from .models import JOB,Company


class job_serializers(serializers.ModelSerializer):
    # Place = serializers.StringRelatedField(many=False)
    # organizationtype = serializers.StringRelatedField(many=False)
    # Browse_cetagory = serializers.StringRelatedField(many=False)
    # Company = serializers.StringRelatedField(many=False)
    
    class Meta:
        model = JOB
        fields= "__all__"
        
        
        
class CompanySerializers(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ['id','company_name','slug']
        
        read_only_fields=['slug']