from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User  
from django.contrib.auth import authenticate       
from django.contrib.auth import login,logout
from .models import Dept, Role, Employee
from django.contrib import messages
from django.contrib.auth.hashers import make_password


# Home page
def home(request):
    return render(request,'home.html')

# User Login
def admin_login(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'admin-login.html', context)
    
    e = request.POST.get('ue')  # retrieve username
    p = request.POST.get('upass')  # retrieve password
    
    user = authenticate(username=e, password=p)  # Authenticate user
    if user:
        if user.is_staff:  # Check for staff privileges
            login(request, user)
            return redirect('/department')  # Redirect to admin dashboard
        context['errormsg'] = "You don't have Admin access"
    else:
        context['errormsg'] = 'Invalid Admin Credentials'
    return render(request, 'admin-login.html', context) 



def user_logout(request):
    logout(request)
    return redirect('/')




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
    dept = Dept.objects.all()
    roles = Role.objects.all()
    emp = Employee.objects.all().order_by('pk')
    return render(request, 'employee.html', {'dept': dept, 'roles': roles, 'emp' : emp})





def add_emp(request):
    if request.method == "POST":
        fn = request.POST.get('fname')
        ln = request.POST.get('lname')
        e = request.POST.get('email')
        mob = request.POST.get('mob')
        dept_id = request.POST.get('dept')
        role_id = request.POST.get('role')
        password = request.POST.get('pass')
        cpass = request.POST.get('cpass')

        print(fn)
        print(ln)
        print(e)
        print(mob)
        print(dept_id)
        print(role_id)
        # print(username)
        print(make_password(password))

        # Check if all fields are filled
        if not all([fn, ln, e, mob, dept_id, role_id, password, cpass]):
            messages.error(request, "All fields are required.")
            return redirect('/employee')

        # Validate mobile number
        if not mob.isdigit() or len(mob) not in [10, 12]:
            messages.error(request, "Invalid mobile number format.")
            return redirect('/employee')
        
        # Check if all fields are filled
        if password != cpass:
            messages.error(request, "Password and Confirm Password should be same")
            return redirect('/employee')
        
        # Validate department and role
        department = Dept.objects.get(dept_id=dept_id)
        role = Role.objects.get(id=role_id)

        # Check for existing username (case insensitive)
        if Employee.objects.filter(email__iexact=e).exists():
            messages.error(request, "Email already taken. Choose a different one.")
            return redirect('/employee')

        # Create and save the Employee
        Employee.objects.create(
            first_name=fn,
            last_name=ln,
            email=e,
            mobile=mob,
            dept_id=dept_id,
            role=role,
            password=make_password(password)  # Secure password hashing
        )

        messages.success(request, "Employee added successfully!")
        return redirect('/employee')

    return render(request, 'employee.html')  # Ensure this template is correct




# Edit Role
def edit_emp(request, eid):
    pass
    # r = Role.objects.get(id=rid)

    # if request.method == "POST":
    #     role = request.POST.get("role_name")
    #     desc = request.POST.get("role_desc")

    #     r.role = role
    #     r.desc = desc
    #     r.save()

    #     return redirect("/role")  












