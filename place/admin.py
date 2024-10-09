from django.contrib import admin
from .models import Place,organizationtype,Browse_cetagory
# Register your models here.

class modelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name','slug']
    

admin.site.register(Place,modelAdmin)

admin.site.register(organizationtype,modelAdmin)

admin.site.register(Browse_cetagory,modelAdmin)