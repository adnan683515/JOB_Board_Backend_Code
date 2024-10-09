from django.contrib import admin
from apply.models import Apply
from django.template.loader import render_to_string
from django.core.mail import  EmailMultiAlternatives
# Register your models here.

class ModelAdminapply(admin.ModelAdmin):
    list_display  = ['user','company_name','phone_number','job_title','status','email','education']
    

    def company_name(self,obj):
        return obj.job.Company
    
    def job_title(self,obj):
        return obj.job.job_title
    
    def status(self,obj):
        return obj.status
    
    def email(self,obj):
        return obj.user.email
    
    
    

    def save_model(self, request, obj, form, change):
        obj.save()
        if obj.status == 'Accepted':
            mail_sub = 'Congress! Your Are Selected In This Job!'
            email_body = render_to_string('accepted_email.html',{'user':obj.user,'job':obj.job})
            email = EmailMultiAlternatives(mail_sub,'',to=[obj.user.email])
            email.attach_alternative(email_body,'text/html')
            email.send()
            
    
admin.site.register(Apply,ModelAdminapply)