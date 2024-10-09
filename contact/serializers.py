from rest_framework import serializers
from .models import contact_Model,our_leaders


class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = contact_Model
        fields = "__all__"
        read_only_fields=['user']
    
    def create(self, validated_data):
        
        print("self contxt data",self.context['request'].user)
        
        validated_data['user'] = self.context['request'].user
        
        print("Contact user",validated_data['user'])
        
        return super().create(validated_data)
    

class OurLeaderSerializers(serializers.ModelSerializer):
    class Meta:
        model = our_leaders
        fields = "__all__"