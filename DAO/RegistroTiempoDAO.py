import os
import sys

# Agrega la carpeta raíz del proyecto al path de Python
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from clases.ClaseRegistroTiempo import RegistroTiempo  # Ajusta si tu archivo tiene otro nombre
from conn.conexion import conexion

def crear_registro_tiempo(fecha, horas, descripcion):
    mi_conexion = conexion()

    if not mi_conexion:
        print("Error de conexión.")
        return False

    cursor = mi_conexion.cursor()

    try:
        sql = """
            INSERT INTO registro_tiempo (fecha, horas, descripcion) 
            VALUES (%s, %s, %s)
        """
        valores = (fecha, horas, descripcion)
        
        cursor.execute(sql, valores)
        mi_conexion.commit()

        print("Registro de tiempo creado exitosamente.")
        return True

    except Exception as e:
        print(f"Error al registrar el tiempo: {e}")
        return False

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if mi_conexion:
            mi_conexion.close()


#------------------------------------------------------------------------------

def buscar_registro_tiempo(id_registro):
    mi_conexion = conexion()

    if not mi_conexion:
        print("Error de conexión.")
        return None

    cursor = mi_conexion.cursor()

    try:
        sql = """
            SELECT id, fecha, horas, descripcion 
            FROM registro_tiempo 
            WHERE id = %s
        """
        valores = (id_registro,)

        cursor.execute(sql, valores)
        resultado = cursor.fetchone()

        if resultado:
            print("Registro de tiempo encontrado:", resultado)
            return resultado
        else:
            print("No se encontró ningún registro de tiempo con ese ID.")
            return None

    except Exception as e:
        print(f"Error al buscar el registro de tiempo: {e}")
        return None

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if mi_conexion:
            mi_conexion.close()


#------------------------------------------------------------------------------

def actualizar_registro_tiempo(id_registro, fecha, horas, descripcion):
    mi_conexion = conexion()

    if not mi_conexion:
        print("Error de conexión.")
        return False

    cursor = mi_conexion.cursor()

    try:
        sql = """
            UPDATE registro_tiempo 
            SET fecha = %s, horas = %s, descripcion = %s 
            WHERE id = %s
        """
        valores = (fecha, horas, descripcion, id_registro)

        cursor.execute(sql, valores)
        mi_conexion.commit()

        if cursor.rowcount > 0:
            print("Registro de tiempo actualizado exitosamente.")
            return True
        else:
            print("No se encontró ningún registro de tiempo con ese ID.")
            return False

    except Exception as e:
        print(f"Error al actualizar el registro de tiempo: {e}")
        return False

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if mi_conexion:
            mi_conexion.close()


#------------------------------------------------------------------------------

def eliminar_registro_tiempo(id_registro):
    mi_conexion = conexion()

    if not mi_conexion:
        print("Error de conexión.")
        return False

    cursor = mi_conexion.cursor()

    try:
        sql = "DELETE FROM registro_tiempo WHERE id = %s"
        valores = (id_registro,)

        cursor.execute(sql, valores)
        mi_conexion.commit()

        if cursor.rowcount > 0:
            print("Registro de tiempo eliminado exitosamente.")
            return True
        else:
            print("No se encontró ningún registro de tiempo con ese ID para eliminar.")
            return False

    except Exception as e:
        print(f"Error al eliminar el registro de tiempo: {e}")
        return False

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if mi_conexion:
            mi_conexion.close()