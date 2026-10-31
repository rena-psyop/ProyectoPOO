import os
import sys

# Agrega la carpeta raíz del proyecto al path de Python
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from clases.ClaseInforme import Informe  # Ajusta si tu archivo tiene otro nombre
from conn.conexion import conexion

def crear_informe(tipo, fecha):
    mi_conexion = conexion()

    if not mi_conexion:
        print("Error de conexión.")
        return False

    cursor = mi_conexion.cursor()

    try:
        sql = """
            INSERT INTO informe (tipo, fecha) 
            VALUES (%s, %s)
        """
        valores = (tipo, fecha)
        
        cursor.execute(sql, valores)
        mi_conexion.commit()

        print("Informe creado exitosamente.")
        return True

    except Exception as e:
        print(f"Error al registrar el informe: {e}")
        return False

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if mi_conexion:
            mi_conexion.close()


#------------------------------------------------------------------------------

def buscar_informe(id_informe):
    mi_conexion = conexion()

    if not mi_conexion:
        print("Error de conexión.")
        return None

    cursor = mi_conexion.cursor()

    try:
        sql = """
            SELECT id, tipo, fecha 
            FROM informe 
            WHERE id = %s
        """
        valores = (id_informe,)

        cursor.execute(sql, valores)
        resultado = cursor.fetchone()

        if resultado:
            print("Informe encontrado:", resultado)
            return resultado
        else:
            print("No se encontró ningún informe con ese ID.")
            return None

    except Exception as e:
        print(f"Error al buscar el informe: {e}")
        return None

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if mi_conexion:
            mi_conexion.close()


#------------------------------------------------------------------------------

def actualizar_informe(id_informe, tipo, fecha):
    mi_conexion = conexion()

    if not mi_conexion:
        print("Error de conexión.")
        return False

    cursor = mi_conexion.cursor()

    try:
        sql = """
            UPDATE informe 
            SET tipo = %s, fecha = %s 
            WHERE id = %s
        """
        valores = (tipo, fecha, id_informe)

        cursor.execute(sql, valores)
        mi_conexion.commit()

        if cursor.rowcount > 0:
            print("Informe actualizado exitosamente.")
            return True
        else:
            print("No se encontró ningún informe con ese ID.")
            return False

    except Exception as e:
        print(f"Error al actualizar el informe: {e}")
        return False

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if mi_conexion:
            mi_conexion.close()


#------------------------------------------------------------------------------

def eliminar_informe(id_informe):
    mi_conexion = conexion()

    if not mi_conexion:
        print("Error de conexión.")
        return False

    cursor = mi_conexion.cursor()

    try:
        sql = "DELETE FROM informe WHERE id = %s"
        valores = (id_informe,)

        cursor.execute(sql, valores)
        mi_conexion.commit()

        if cursor.rowcount > 0:
            print("Informe eliminado exitosamente.")
            return True
        else:
            print("No se encontró ningún informe con ese ID para eliminar.")
            return False

    except Exception as e:
        print(f"Error al eliminar el informe: {e}")
        return False

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if mi_conexion:
            mi_conexion.close()