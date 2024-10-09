from rest_framework import serializers
from .models import Browse_cetagory,Place,organizationtype,work_type


class BrowseCetagorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Browse_cetagory
        fields = "__all__"
            


class PlaceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = "__all__"
            
            
            
class OrganaigationSerializers(serializers.ModelSerializer):
    class Meta:
        model = organizationtype
        fields = "__all__"
            
            
class WorkSerializers(serializers.ModelSerializer):
    class Meta:
        model = work_type
        fields = "__all__"
            