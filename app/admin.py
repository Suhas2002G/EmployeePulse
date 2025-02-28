from django.contrib import admin
from .models import Dept, Role

class DeptAdmin(admin.ModelAdmin):
    list_display = ['dept_id','dept_name','desc','status', 'created_at', 'updated_at']
    list_filter = ['dept_name','status']
    search_fields = ['dept_name']
    
class RoleAdmin(admin.ModelAdmin):
    list_display = ['uid','role','desc','created_at','updated_at']
    list_filter = ['uid','role']
    search_fields = ['uid','role']

admin.site.register(Dept,DeptAdmin)
admin.site.register(Role,RoleAdmin)
