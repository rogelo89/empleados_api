from rest_framework import serializers


class EmpleadoSerializer(serializers.Serializer):
    Id_Empleado = serializers.CharField()
    No_CI = serializers.CharField()
    Nombre = serializers.CharField()
    Apellido_1 = serializers.CharField()
    Apellido_2 = serializers.CharField()
    Baja = serializers.BooleanField()
    Alta = serializers.BooleanField()
    Id_Direccion = serializers.CharField()
    Sexo = serializers.CharField()
    Id_Provincia = serializers.CharField()
    Id_Municipio = serializers.CharField()
    Docente = serializers.BooleanField()
    Desc_Provincia = serializers.CharField(required=False)
    Desc_Municipio = serializers.CharField(required=False)
    Desc_Direccion = serializers.CharField(required=False)
