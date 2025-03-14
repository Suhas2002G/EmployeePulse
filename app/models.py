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
    role = models.ForeignKey(Role, on_delete=models.CASCADE, db_column='rid')
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE, db_column='did')
    doj = models.DateField(auto_now_add=True)


# Task Model
class Task(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=5000)
    priority = models.CharField(max_length=20, choices=(('High','High'),('Low','Low'),('Medium','Medium')))
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='assigned_to')
    start_date = models.DateField()
    end_date = models.DateField()
    task_type = models.CharField(max_length=20, choices=(('Team','Team'),('Individual','Individual')))
    status = models.CharField(max_length=15, choices=(('Pending','Pending'),
                                                      ('In-Progress','In-Progress'),
                                                      ('Completed','Completed'))
                                                      , default='Pending')



class Reveive(models.Model):
    eid = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='eid')
    reveive_period = models.CharField(max_length=20, null=True)
    rating = models.IntegerField()
    improvement = models.CharField(max_length=2000)
    reveive_date = models.DateTimeField(auto_now_add=True)



class Leave(models.Model):
    TYPE = (('SL','SL'),("PL","PL"),('CL','CL'))
    eid = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='eid')
    reason = models.CharField(max_length=2000)
    from_date = models.DateField()
    to_date = models.DateField()
    leave_type = models.CharField(max_length=200, choices=TYPE)
    status = models.CharField(max_length=200, default='Pending', choices=(("Approved","Approved"),('Rejected','Rejected')))


# To Otp while Forget Password 
class Otp(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    otp = models.CharField(max_length=4)