from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser   


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
        return f'{self.uid.username} : {self.role}'
 

class Employee(AbstractUser):
    username = None   # this is ensure login will not happen through username
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10, unique=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    doj = models.DateField(auto_now_add=True)

    USERNAME_FIELD = 'email'  # this is ensure login will happen through email id
    REQUIRED_FIELDS = []
    # objects = UserManager()
    def __str__(self):
        return self.email
    
# Now we have to create model manager for this models class
# create manager.py file into app directory




