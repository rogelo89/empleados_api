from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .db_utils import get_empleados, get_empleado_by_id
from .serializers import EmpleadoSerializer


@cache_page(60 * 1440)
@vary_on_cookie
@api_view(['GET'])
def empleado_list(request):
    empleados = get_empleados()
    # Filtrar empleados activos
    active_employees = [emp for emp in empleados if not emp['Baja']]
    serializer = EmpleadoSerializer(active_employees, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def empleado_detail(request, id_empleado):
    empleado = get_empleado_by_id(id_empleado)

    if not empleado:
        return Response(
            {'error': 'Empleado no encontrado'},
            status=status.HTTP_404_NOT_FOUND
        )

    if empleado['Baja']:
        return Response(
            {
                'error': 'Empleado dado de baja del centro',
                'detalle': 'Este empleado no está activo en el sistema'
            },
            status=status.HTTP_403_FORBIDDEN
        )

    serializer = EmpleadoSerializer(empleado)
    return Response(serializer.data)
