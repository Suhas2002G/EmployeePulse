from django.contrib import admin
from .models import Dept


class DeptAdmin(admin.ModelAdmin):
    list_display = ['dept_id','dept_name','desc','status', 'created_at', 'updated_at']
    list_filter = ['dept_name','status']
    search_fields = ['dept_name']


admin.site.register(Dept,DeptAdmin)
