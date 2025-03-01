from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home),
    path('dashboard', views.dashboard),
    path('department', views.department),
    path('add_dept', views.add_dept),
    path('del_dept/<did>', views.del_dept),
    path('edit/<did>', views.edit),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
