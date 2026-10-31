import os
import sys

# Agrega la carpeta raíz del proyecto al path de Python
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from clases.ClaseProyecto import Proyecto  # Ajusta si tu archivo tiene otro nombre
from conn.conexion import conexion

def crear_proyecto(nombre_proyecto, descripcion, fecha_inicio_proyecto):
    mi_conexion = conexion()

    if not mi_conexion:
        print("Error de conexión.")
        return False

    cursor = mi_conexion.cursor()

    try:
        sql = """
            INSERT INTO proyecto (nombre_proyecto, descripcion, fecha_inicio_proyecto) 
            VALUES (%s, %s, %s)
        """
        valores = (nombre_proyecto, descripcion, fecha_inicio_proyecto)
        
        cursor.execute(sql, valores)
        mi_conexion.commit()

        print("Proyecto creado exitosamente.")
        return True

    except Exception as e:
        print(f"Error al registrar el proyecto: {e}")
        return False

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if mi_conexion:
            mi_conexion.close()


#------------------------------------------------------------------------------

def buscar_proyecto(id_proyecto):
    mi_conexion = conexion()

    if not mi_conexion:
        print("Error de conexión.")
        return None

    cursor = mi_conexion.cursor()

    try:
        sql = """
            SELECT id, nombre_proyecto, descripcion, fecha_inicio_proyecto 
            FROM proyecto 
            WHERE id = %s
        """
        valores = (id_proyecto,)

        cursor.execute(sql, valores)
        resultado = cursor.fetchone()

        if resultado:
            print("Proyecto encontrado:", resultado)
            return resultado
        else:
            print("No se encontró ningún proyecto con ese ID.")
            return None

    except Exception as e:
        print(f"Error al buscar el proyecto: {e}")
        return None

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if mi_conexion:
            mi_conexion.close()


#------------------------------------------------------------------------------

def actualizar_proyecto(id_proyecto, nombre_proyecto, descripcion, fecha_inicio_proyecto):
    mi_conexion = conexion()

    if not mi_conexion:
        print("Error de conexión.")
        return False

    cursor = mi_conexion.cursor()

    try:
        sql = """
            UPDATE proyecto 
            SET nombre_proyecto = %s, descripcion = %s, fecha_inicio_proyecto = %s 
            WHERE id = %s
        """
        valores = (nombre_proyecto, descripcion, fecha_inicio_proyecto, id_proyecto)

        cursor.execute(sql, valores)
        mi_conexion.commit()

        if cursor.rowcount > 0:
            print("Proyecto actualizado exitosamente.")
            return True
        else:
            print("No se encontró ningún proyecto con ese ID.")
            return False

    except Exception as e:
        print(f"Error al actualizar el proyecto: {e}")
        return False

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if mi_conexion:
            mi_conexion.close()


#------------------------------------------------------------------------------

def eliminar_proyecto(id_proyecto):
    mi_conexion = conexion()

    if not mi_conexion:
        print("Error de conexión.")
        return False

    cursor = mi_conexion.cursor()

    try:
        sql = "DELETE FROM proyecto WHERE id = %s"
        valores = (id_proyecto,)

        cursor.execute(sql, valores)
        mi_conexion.commit()

        if cursor.rowcount > 0:
            print("Proyecto eliminado exitosamente.")
            return True
        else:
            print("No se encontró ningún proyecto con ese ID para eliminar.")
            return False

    except Exception as e:
        print(f"Error al eliminar el proyecto: {e}")
        return False

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if mi_conexion:
            mi_conexion.close()