import os
import sys

# Agrega la carpeta raíz del proyecto al path de Python
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from clases.ClaseDepartamento import Departamento
from conn.conexion import conexion

def crearDepartamento(nombreDepa):
    mi_conexion = conexion()

    if not mi_conexion:
        print("Error de conexión.")
        return False

    cursor = mi_conexion.cursor()

    try:
        sql = "INSERT INTO departamento (nombreDepa) values (%s)"
        valores = (nombreDepa,)
        cursor.execute(sql, valores)

        mi_conexion.commit()

        print("Departamento creado exitosamente.")
        return True

    except Exception as e:
        print(f"Error al registrar {e}")
        return False

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if mi_conexion:
            mi_conexion.close()


#------------------------------------------------------------------------------

def buscarDepartamento(id_departamento):
    mi_conexion = conexion()

    if not mi_conexion:
        print("Error de conexión.")
        return False

    cursor = mi_conexion.cursor()

    try:
        sql = "SELECT id, nombreDepa FROM departamento WHERE id = %s"
        valores = (id_departamento,)

        cursor.execute(sql, valores)
        
        resultado = cursor.fetchone()

        if resultado:
            print("Departamento encontrado:", resultado)
            return resultado
        else:
            print("No se encontró ningún departamento con ese ID.")
            return None

    except Exception as e:
        print(f"Error al buscar el departamento: {e}")
        return None

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if mi_conexion:
            mi_conexion.close()


#------------------------------------------------------------------------------


def actualizar_departamento(id_departamento, nuevo_nombreDepa):
    mi_conexion = conexion()

    if not mi_conexion:
        print("Error de conexión.")
        return False

    cursor = mi_conexion.cursor()

    try:
        sql = "UPDATE departamento SET nombreDepa = %s WHERE id = %s"
        valores = (nuevo_nombreDepa, id_departamento)

        cursor.execute(sql, valores)
        mi_conexion.commit()  

        if cursor.rowcount > 0:
            print("Departamento actualizado exitosamente.")
            return True
        else:
            print("No se encontró ningún departamento con ese ID.")
            return False

    except Exception as e:
        print(f"Error al actualizar el departamento: {e}")
        return False

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if mi_conexion:
            mi_conexion.close()


#------------------------------------------------------------------------------


def eliminar_departamento(id_departamento):
    mi_conexion = conexion()

    if not mi_conexion:
        print("Error de conexión.")
        return False

    cursor = mi_conexion.cursor()

    try:
        sql = "DELETE FROM departamento WHERE id = %s"
        valores = (id_departamento,)

        cursor.execute(sql, valores)
        mi_conexion.commit()  

        if cursor.rowcount > 0:
            print("Departamento eliminado exitosamente.")
            return True
        else:
            print("No se encontró ningún departamento con ese ID para eliminar.")
            return False

    except Exception as e:
        print(f"Error al eliminar el departamento: {e}")
        return False

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if mi_conexion:
            mi_conexion.close()