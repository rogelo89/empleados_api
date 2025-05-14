from django.db import models


class RH_Provincia(models.Model):
    Id_Provincia = models.CharField(max_length=5, primary_key=True)
    Desc_Provincia = models.CharField(max_length=50)
    RepMovPendular = models.BooleanField()

    class Meta:
        db_table = 'RH_Provincias'
        managed = False


class RH_Municipio(models.Model):
    Id_Provincia = models.CharField(max_length=5)  # No es FK formal
    Id_Municipio = models.CharField(max_length=5)
    Desc_Municipio = models.CharField(max_length=50)

    class Meta:
        db_table = 'RH_Municipios'
        managed = False
        unique_together = (('Id_Provincia', 'Id_Municipio'),)


class RH_Plantilla(models.Model):
    Nivel = models.SmallIntegerField()
    Id_Direccion = models.CharField(max_length=15)
    Desc_Direccion = models.CharField(max_length=100)
    Id_Clave = models.CharField(max_length=17, unique=True)

    class Meta:
        db_table = 'RH_Plantilla'
        managed = False
        unique_together = (('Nivel', 'Id_Direccion'),)


class RH_Cargos(models.Model):
    Id_Cargo = models.CharField(max_length=5, primary_key=True)
    Desc_Cargo = models.CharField(max_length=120)

    class Meta:
        db_table = 'RH_Cargos'
        managed = False


class RH_Categorias_Docente_Invest(models.Model):
    Id_Categoria_DI = models.CharField(max_length=5, primary_key=True)
    Desc_Categoria_DI = models.CharField(max_length=50)

    class Meta:
        db_table = 'RH_Categorias_Docente_Invest'
        managed = False


class RH_Grados_Cientificos(models.Model):
    Id_Grado_Cientifico = models.CharField(max_length=5, primary_key=True)
    Desc_Grado_Cientifico = models.CharField(max_length=50)

    class Meta:
        db_table = 'RH_Grados_Cientificos'
        managed = False


class Empleados_Gral(models.Model):
    Id_Empleado = models.CharField(max_length=15, primary_key=True)
    No_CI = models.CharField(max_length=15)
    Nombre = models.CharField(max_length=50)
    Apellido_1 = models.CharField(max_length=50)
    Baja = models.BooleanField()
    Alta = models.BooleanField()
    Id_Cargo = models.CharField(max_length=5)
    Id_Direccion = models.CharField(max_length=15)
    Sexo = models.CharField(max_length=1)
    Id_Provincia = models.CharField(max_length=5)
    Id_Municipio = models.CharField(max_length=5)
    Docente = models.BooleanField()
    Id_Categoria_DI = models.CharField(max_length=5)
    Apellido_2 = models.CharField(max_length=50)
    Id_Grado_Cientifico = models.CharField(max_length=5)

    class Meta:
        db_table = 'Empleados_Gral'
        managed = False
