from django.db import models


# Department Model
class Dept(models.Model):
    CAT = (('IT','IT'),('Support','Support'),('Sales','Sales'))
    dept_id = models.BigAutoField(primary_key=True)
    dept_name = models.CharField(max_length=100, choices=CAT)
    desc = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  
    status = models.BooleanField(default=True)  
    
    def __str__(self):
        return self.dept_name

