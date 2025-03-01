from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User        
from django.contrib.auth import authenticate       
from django.contrib.auth import login,logout
from .models import Dept



# Home page
def home(request):
    return render(request,'home.html')


def dashboard(request):
    return render(request, 'dashboard.html')


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
    


