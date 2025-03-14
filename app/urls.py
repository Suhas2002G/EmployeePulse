from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home),
    path('user_login', views.user_login),
    path('user_logout', views.user_logout),
    path('department', views.department),
    path('add_dept', views.add_dept),
    path('del_dept/<did>', views.del_dept),
    path('edit/<did>', views.edit),
    path('forgetpass', views.forgetpass),
    path('sendOTP', views.sendOTP),
    path('verify-otp', views.verify_otp),
    path('setPass', views.setPass),
    path('role', views.role),
    path('add_role', views.add_role),
    path('del_role/<rid>', views.del_role),
    path('editrole/<rid>', views.editrole),

    path('employee', views.employee),
    path('add_emp', views.add_emp),
    path('del_emp/<eid>', views.del_emp),
    path('edit_emp/<eid>', views.edit_emp),


    path('task', views.task),
    # path('addtask_form', views.addtask_form),
    path('add_task', views.add_task),


    path('reveive', views.reveive),
    path('reveive-dash', views.reveive_dash),


    path('leave-dash', views.leave_dash),
    path('status/<id>/<ch>', views.status),

    path('apply_for_leave', views.apply_for_leave),


    # path('emp_dash', views.emp_dash),
    # path('emp-leave', views.emp_leave),
    # path('emp-review', views.emp_review),
    # path('emp-task', views.emp_task),

]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
