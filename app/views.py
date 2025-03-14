from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User  
from django.contrib.auth import authenticate       
from django.contrib.auth import login,logout
from .models import Dept, Role, Employee, Task, Reveive, Leave, Otp
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from datetime import date
import os
import datetime
import random
from django.core.mail import send_mail

# Home page
def home(request):
    return render(request,'home2.html')

# User Login
def user_login(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'login.html', context)
    
    if request.method == 'POST':
        e = request.POST.get('ue')  # retrieve username
        p = request.POST.get('upass')  # retrieve password
        # r = request.POST.get('role')

        # print(r)
        user = authenticate(username=e, password=p)  # Authenticate user
        if user:
            if user.is_staff:  # Check for staff privileges
                login(request, user)
                return redirect('/task')  # Redirect to admin dashboard
            context['errormsg'] = "You don't have Admin access"
        else:
            context['errormsg'] = 'Invalid Admin Credentials'
        return render(request, 'login.html', context)
        # if r == 'admin':
        #     user = authenticate(username=e, password=p)  # Authenticate user
        #     if user:
        #         if user.is_staff:  # Check for staff privileges
        #             login(request, user)
        #             return redirect('/task')  # Redirect to admin dashboard
        #         context['errormsg'] = "You don't have Admin access"
        #     else:
        #         context['errormsg'] = 'Invalid Admin Credentials'
        #     return render(request, 'login.html', context)  # Render the login page with error message
        # else:
        #     u=authenticate(username=e,password=p) # For Authentication Purpose
        #     if u is not None:
        #         login(request,u)        # Login Method
        #         return redirect('/emp-task')
        #         # return HttpResponse('emp fetched')
        #     else:
        #         context['errormsg']='Invalid Credential'
        #         return render(request,'login.html',context)




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
    if request.method == 'POST':
        # Get form data
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        mobile = request.POST.get('mob')
        dept_id = request.POST.get('dept')
        role_id = request.POST.get('role')
        password = request.POST.get('pass')
        confirm_password = request.POST.get('cpass')

        # Validate passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('/employee')

        try:
            # Create user
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )

            # Get department and role objects
            department = Dept.objects.get(dept_id=int(dept_id))  # ✅ Convert ID to integer
            role = Role.objects.get(id=int(role_id))  # ✅ Convert ID to integer

            # Create employee (Assigning ForeignKey fields correctly)
            Employee.objects.create(
                uid=user,
                mobile=mobile,
                dept=department,  # ✅ Assigning the instance
                role=role,  # ✅ Assigning the instance
                doj=user.date_joined
            )
            frm='suhas8838@gmail.com'
            messages.success(request, f"Employee {first_name} {last_name} added successfully")
            send_mail(
                'Welcome to EmployeePulse',
                f"Welcome to our company..! Your Username : {email} and Password : {password} ",
                frm,
                [email],
                fail_silently=False,
                )


        except Exception as e:
            messages.error(request, f"Error adding employee: {str(e)}")

        return redirect('/employee')

    # If GET request (shouldn't happen directly)
    return redirect('/employee')





def del_emp(request, eid):
    try:
        employee = Employee.objects.get(id=eid)
        employee.delete()

        messages.success(request, f"Employee {employee.uid.first_name} {employee.uid.last_name} deleted successfully")
    except Exception as e:
        messages.error(request, f"Error deleting employee: {str(e)}")
    
    return redirect('/employee')  





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






def forgetpass(request):
    return render(request, 'forget-password.html')



def sendOTP(request):
    context = {}
    if request.method == "POST":
        e = request.POST.get("uemail")

        # Check if user exists
        if User.objects.filter(email=e).exists():
            otp = str(random.randint(1000, 9999))
            frm='suhas8838@gmail.com'
            # Save OTP 
            Otp.objects.create(otp=otp, email=e)

            # Store email in session
            request.session['reset_email'] = e  

            # Send OTP to user email
            send_mail(
                'Reset Password',
                f"Your OTP for password reset is: {otp}",
                frm,
                [e],
                fail_silently=False,
            )

            return redirect('/verify-otp')  # Redirect without email in URL
        else:
            context['errormsg'] = 'This email ID is not registered with us!'
            return render(request, 'forget-password.html', context)



def verify_otp(request):
    context = {}
    e = request.session.get('reset_email')   # Retrieve email from session
    if not e:
        return redirect('/forgetpass')  # Redirect if email is missing

    if request.method == 'POST':
        input_otp = request.POST.get('otp')
        otp_entry = Otp.objects.filter(email=e).order_by('-created_at').first()
 
        if otp_entry.otp == input_otp:
            return redirect('/setPass')  # Redirect to password reset page
        else:
            context['error_message'] = 'Incorrect OTP. Please try again.'
    return render(request, 'verify-otp.html', context)




def setPass(request):
    context = {}
    e = request.session.get('reset_email')  # Retrieve email from session
    if not e:
        return redirect('/forgetpass')
    
    if request.method == 'GET':
        return render(request, 'setPass.html')
    else:
        p = request.POST.get('pass', '')
        cp = request.POST.get('cpass', '')

        if p=='' or cp=='':
            context['error_message'] = 'Please fill in all fields.'
        elif p != cp:
            context['error_message'] = 'Passwords do not match.'
        else:
            try:
                user = User.objects.filter(email=e).first()
                if user:
                    user.set_password(p)
                    user.save()
                    request.session.flush()  # Clear session data after successful reset
                    context['success_message'] = 'Password Successfully Reset.'
                    return render(request,'setPass.html', context)  # Redirect to login page
                    
                else:
                    context['error_message'] = 'User not found.'
            except Exception as err:
                context['error_message'] = 'An error occurred. Please try again.'

    return render(request, 'setPass.html', context)












def task(request):
    context={}
    emp = Employee.objects.all()
    # print(emp)
    context['emp']=emp

    task = Task.objects.all()
    context['task']=task

    pending_task = Task.objects.filter(status='Pending').count()
    in_progress_task = Task.objects.filter(status='In-Progress').count()
    completed_task = Task.objects.filter(status='Completed').count()

    context['pending_task']= pending_task
    context['in_progress_task']=in_progress_task
    context['completed_task']=completed_task
    return render(request, 'task.html',context)





def add_task(request):
    context={}
    if request.method == 'GET':
        emp = Employee.objects.all()
        context['emp']=emp
        return render(request, 'add_task.html', context)
    if request.method == "POST":
        task_name = request.POST.get("tname")
        priority = request.POST.get("priority")
        assigned_to_id = request.POST["assigned_to"]
        task_type = request.POST.get("task_type")
        start_date = request.POST.get("start_date")
        due_date = request.POST.get("due_date")
        description = request.POST.get("desc")

        print(task_name)
        print(priority)
        print(f'this is eid {assigned_to_id}')
        print(task_type)
        print(start_date)
        print(due_date)
        print(description)

        # Validate assigned_to employee
        try:
            assigned_to = Employee.objects.get(uid=assigned_to_id)
            print(assigned_to)
        except Employee.DoesNotExist:
            messages.error(request, "Error occured.")
            return redirect("/task")  # Replace with actual task listing page name

        # Create new task
        Task.objects.create(
            title=task_name,
            priority=priority,
            assigned_to=assigned_to,
            task_type=task_type,
            start_date=start_date,
            end_date=due_date,
            desc=description
        )

        messages.success(request, "Task created successfully!")
        return redirect("/task")  # Replace with actual task listing page

    return redirect("/task")  # Fallback for GET requests







def reveive_dash(request):
    context={}
    reveive = Reveive.objects.all()
    context['reveive']=reveive
    return render(request, 'reveive-dash.html',context)





def reveive(request):
    if request.method == 'GET':
        context={}
        emp= Employee.objects.all()
        context['emp']=emp
        return render(request, 'reveive.html', context)
    if request.method == 'POST':
        emp = request.POST.get('emp')
        period = request.POST.get('reviewPeriod')
        rating = request.POST.get('techSkill')
        improvement = request.POST.get('improvement')

        print(emp)
        print(period)
        print(rating)
        print(improvement)

        eid = Employee.objects.get(id=emp)
        print(eid)

        Reveive.objects.create(
            eid=eid,
            rating=rating,
            reveive_period = period,
            improvement=improvement
        )


        return redirect('/reveive-dash')




def leave_dash(request):
    context={}
    return render(request, 'leave-dash.html', context)









def leave_dash(request):
    context={}
    leave = Leave.objects.all()
    context['leave']=leave

    return render(request, 'leave-dash.html', context)



def status(request,id,ch):
    l = Leave.objects.get(id=id)
    print(l)
    if ch == '0':
        l.status='Approve'
        l.save()
    if ch == '1' : 
        l.status='Reject'
        l.save()
    return redirect('/leave-dash')


def apply_for_leave(request):
    context={}
    if request.method == "GET":
        # leave = Leave.objects.all()
        leave = Leave.TYPE
        context['leave']=leave
        return render ( request, 'leave-form.html', context)
    if request.method == "POST":
        emp = Employee.objects.get(uid=request.user.id)

        type = request.POST.get('type')
        reason = request.POST.get('reason')
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')

        print(emp)
        print(type)
        print(reason)
        print(from_date)
        print(to_date)

        Leave.objects.create(
            eid=emp,
            leave_type=type,
            from_date = from_date,
            to_date=to_date,
            status = 'Pending',
            reason=reason

        )

        return redirect('/leave-dash')
    



# def emp_dash(request):
#     context={}
#     return render(request, 'emp-dash.html', context)



# def emp_task(request):
#     context={}
#     task = Task.objects.filter(assigned_to=request.user.id)
#     context['task']=task
#     return render(request, 'emp-task.html', context)



# def emp_review(request):
#     context={}
#     return render(request, 'emp-review.html', context)



# def emp_leave(request):
#     context={}
#     return render(request, 'emp-leave.html', context)