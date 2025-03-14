from django.contrib import admin
from .models import Dept, Role, Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','uid','mobile','dept', 'role', 'doj']


class DeptAdmin(admin.ModelAdmin):
    list_display = ['dept_id','dept_name','desc','status', 'created_at', 'updated_at']
    list_filter = ['dept_name','status']
    search_fields = ['dept_name']
    
class RoleAdmin(admin.ModelAdmin):
    list_display = ['role','desc','created_at','updated_at']
    list_filter = ['role']
    search_fields = ['role']

admin.site.register(Dept,DeptAdmin)
admin.site.register(Role,RoleAdmin)
admin.site.register(Employee,EmployeeAdmin)
