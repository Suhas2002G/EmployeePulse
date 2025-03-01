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

def department(request):
    context={}
    d = Dept.objects.all().order_by('dept_id')
    context['data']=d
    return render(request, 'department.html',context)



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



def del_dept(request, did):
    dept = Dept.objects.get(dept_id = did) 
    dept.delete()

    return redirect('/department')


def edit(request, did):
    department = Dept.objects.get(dept_id=did)

    if request.method == "POST":
        dept_name = request.POST.get("dept_name")
        dept_desc = request.POST.get("dept_desc")

        department.dept_name = dept_name
        department.desc = dept_desc
        department.save()

        return redirect("/department")  

    # return render(request, "edit_department.html", {"department": department})