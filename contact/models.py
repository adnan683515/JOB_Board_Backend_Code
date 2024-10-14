from django.db import models
from django.contrib.auth.models import User
from rest_framework.pagination import PageNumberPagination
# Create your models here.



class contact_Model(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=12,null=True,blank=True)
    email = models.CharField(max_length=200,null=True,blank=True)
    Your_message = models.TextField()
    
    

    def __str__(self):
        return self.user.username
    
    



    

class our_leaders(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=40)
    image = models.ImageField(upload_to="leaders")
    descriptions = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return self.name
    
class commnet(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    our_leaders = models.ForeignKey(our_leaders,on_delete=models.CASCADE)
    text = models.TextField()
    