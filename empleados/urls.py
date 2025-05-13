from django.urls import path
from .views import empleado_list, empleado_detail

urlpatterns = [
    path('empleados/', empleado_list, name='empleado-list'),
    path('empleados/<str:id_empleado>/',
         empleado_detail, name='empleado-detail'),
]
