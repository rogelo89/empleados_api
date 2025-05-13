import pyodbc
from django.conf import settings
from contextlib import contextmanager


@contextmanager
def get_db_connection():
    conn = None
    try:
        conn_str = (
            f'DRIVER={settings.DB_DRIVER};'
            f'SERVER={settings.DB_HOST};'
            f'DATABASE={settings.DB_NAME};'
            f'UID={settings.DB_USER};'
            f'PWD={settings.DB_PASSWORD}'
        )
        conn = pyodbc.connect(conn_str)
        yield conn
    except pyodbc.Error as e:
        print(f"Error de conexión: {e}")
        raise
    finally:
        if conn:
            conn.close()


def execute_query(query, params=None):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        # Obtener nombres de columnas
        columns = [column[0] for column in cursor.description]

        # Convertir resultados a lista de diccionarios
        results = []
        for row in cursor.fetchall():
            results.append(dict(zip(columns, row)))

        return results


def get_empleados():
    query = """
    SELECT 
        e.*,
        p.Desc_Provincia,
        m.Desc_Municipio,
        pl.Desc_Direccion
    FROM Empleados_Gral e
    LEFT JOIN RH_Provincias p ON e.Id_Provincia = p.Id_Provincia
    LEFT JOIN RH_Municipios m ON e.Id_Provincia = m.Id_Provincia AND e.Id_Municipio = m.Id_Municipio
    LEFT JOIN RH_Plantilla pl ON e.Id_Direccion = pl.Id_Direccion
    """
    return execute_query(query)


def get_empleado_by_id(empleado_id):
    query = """
    SELECT 
        e.*,
        p.Desc_Provincia,
        m.Desc_Municipio,
        pl.Desc_Direccion
    FROM Empleados_Gral e
    LEFT JOIN RH_Provincias p ON e.Id_Provincia = p.Id_Provincia
    LEFT JOIN RH_Municipios m ON e.Id_Provincia = m.Id_Provincia AND e.Id_Municipio = m.Id_Municipio
    LEFT JOIN RH_Plantilla pl ON e.Id_Direccion = pl.Id_Direccion
    WHERE e.Id_Empleado = ?
    """
    results = execute_query(query, (empleado_id,))
    return results[0] if results else None
