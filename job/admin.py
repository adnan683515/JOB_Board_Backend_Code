from django.contrib import admin
from .models import JOB,Company
# Register your models here.

admin.site.register(JOB)

class Company_ModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('company_name',)}
    list_display = ['company_name','slug']
    
admin.site.register(Company,Company_ModelAdmin)