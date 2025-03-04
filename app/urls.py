from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home),
    path('department', views.department),
    path('add_dept', views.add_dept),
    path('del_dept/<did>', views.del_dept),
    path('edit/<did>', views.edit),

    path('role', views.role),
    path('add_role', views.add_role),
    path('del_role/<rid>', views.del_role),
    path('editrole/<rid>', views.editrole),

    path('employee', views.employee),
    path('add_emp', views.add_emp),
    # path('del_emp/<eid>', views.del_emp),
    path('edit_emp/<eid>', views.edit_emp),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
