from rest_framework import serializers
from job.serializers import job_serializers,CompanySerializers
from .models import Apply
from job.models import JOB


class ApplySerializers(serializers.ModelSerializer):
    job = job_serializers(read_only=True)
    
    class Meta:
        model = Apply
        fields=['job','phone_number','image','status','title','company','office_location', 'education','facebookLink','resume']
        read_only_fields=['user']
        

    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    
    
    
    
    
    
    
    

class appy_serializer_new(serializers.ModelSerializer):
    class Meta:
        model = Apply
        fields = ['user','job','phone_number','image','status','title','company','office_location', 'education','facebookLink','resume']
        
    
    def create(self, validated_data):
        user= self.context['request'].user
        print(user)
        job_id = validated_data.pop('job')  # Extract job_id
        print(job_id)
        job = JOB.objects.get(id=29)  # Get the job instance''
        print(job)
        apply_instance = Apply.objects.create(job=job, user=user, **validated_data)  # Create the apply instance
        return apply_instance