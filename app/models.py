from django.db import models
from django.contrib.auth.models import User 


# Department Model : 
class Dept(models.Model):
    dept_id = models.BigAutoField(primary_key=True)
    dept_name = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  
    status = models.BooleanField(default=True)  
    
    def __str__(self):
        return self.dept_name


# Role Model : 
class Role(models.Model):
    role = models.CharField(max_length=100)
    desc = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.role}'
 

# Employee Model : 
class Employee(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE, db_column='uid')
    mobile = models.CharField(max_length=10, unique=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    doj = models.DateField(auto_now_add=True)







