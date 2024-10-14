from rest_framework import serializers
from .models import Browse_cetagory,Place,organizationtype,work_type


class BrowseCetagorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Browse_cetagory
        fields = ['id','name','slug']
        
        read_only_fields=['slug']
            


class PlaceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['id','name','slug']
        
        read_only_fields=['slug']
            
            
            
class OrganaigationSerializers(serializers.ModelSerializer):
    class Meta:
        model = organizationtype
        fields = ['id','name','slug']
            
            
class WorkSerializers(serializers.ModelSerializer):
    class Meta:
        model = work_type
        fields = "__all__"
            