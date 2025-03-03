from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User  
# since we have created CustomUser model therefore we need to to upate User model
from django.contrib.auth import get_user_model 
User = get_user_model() 


from django.contrib.auth import authenticate       
from django.contrib.auth import login,logout
from .models import Dept, Role



# Home page
def home(request):
    return render(request,'home.html')



# Display all Departments
def department(request):
    context={}
    d = Dept.objects.all().order_by('dept_id')
    context['data']=d
    return render(request, 'department.html',context)


# Add new Department
def add_dept(request):
    if request.method == 'POST':
        context = {} 

        dname = request.POST.get('dept_name')
        desc = request.POST.get('dept_desc')

        if not dname or not desc:
            context['errormsg'] = 'Fill all the fields'
        else:
            Dept.objects.create(dept_name=dname, desc=desc)
            context['success'] = 'New Department has been Added..!'
        return redirect('/department') 

    return render(request, 'department.html', context)  # Handle non-POST requests


# Delete Department
def del_dept(request, did):
    dept = Dept.objects.get(dept_id = did) 
    dept.delete()
    return redirect('/department')


# Edit Department
def edit(request, did):
    d = Dept.objects.get(dept_id=did)

    if request.method == "POST":
        dept_name = request.POST.get("dept_name")
        dept_desc = request.POST.get("dept_desc")

        d.dept_name = dept_name
        d.desc = dept_desc
        d.save()

        return redirect("/department")  
    


# Display all Roles
def role(request):
    context={}
    r = Role.objects.all().order_by('id')
    context['data'] = r
    return render(request, 'role.html', context)


# Add new Role
def add_role(request):
    if request.method == 'POST':
        context = {} 

        rname = request.POST.get('role_name')
        desc = request.POST.get('role_desc')

        if not rname or not desc:
            context['errormsg'] = 'Fill all the fields'
        else:
            Role.objects.create(role=rname, desc=desc)
            context['success'] = 'New Role has been Added..!'
        return redirect('/role') 

    return render(request, 'role.html', context)


# Delete Role
def del_role(request, rid):
    role = Role.objects.get(id = rid) 
    role.delete()
    return redirect('/role')


# Edit Role
def editrole(request, rid):
    r = Role.objects.get(id=rid)

    if request.method == "POST":
        role = request.POST.get("role_name")
        desc = request.POST.get("role_desc")

        r.role = role
        r.desc = desc
        r.save()

        return redirect("/role")  
    


def employee(request):
    return render(request, 'employee.html')