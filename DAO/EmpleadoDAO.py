import os
import sys

# Agrega la carpeta raíz del proyecto al path de Python
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from clases.ClaseEmpleado import Empleado
from conn.conexion import conexion

def validacion(correo_ingresado, contrasena_ingresada):
  mi_conexion = conexion()

  if not mi_conexion:
    print("Error de conexión.")
    return False

  cursor = mi_conexion.cursor()

  try:
    sql = "SELECT correo, contrasena FROM empleado WHERE correo = %s AND contrasena = %s"
    # Aquí se usan los parámetros que recibe la función
    cursor.execute(sql, (correo_ingresado, contrasena_ingresada))
    resultado = cursor.fetchone()

    if resultado:
      return True
    else:
      return False

  except Exception as e:
    print(f"Ocurrió un error: {e}")
    return False

  finally:
    cursor.close()
    mi_conexion.close()

def crear_empleado(nombre, direccion, telefono, correo, contrasena, rol, fecha_inicio, salario):
    mi_conexion = conexion()

    if not mi_conexion:
        print("Error de conexión.")
        return False

    cursor = mi_conexion.cursor()

    try:
        sql = """
            INSERT INTO empleado (nombre, direccion, telefono, correo, contrasena, rol, fecha_inicio, salario) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        valores = (nombre, direccion, telefono, correo, contrasena, rol, fecha_inicio, salario)
        
        cursor.execute(sql, valores)
        mi_conexion.commit()

        print("Empleado creado exitosamente.")
        return True

    except Exception as e:
        print(f"Error al registrar el empleado: {e}")
        return False

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if mi_conexion:
            mi_conexion.close()


#------------------------------------------------------------------------------

def buscar_empleado(id_empleado):
    mi_conexion = conexion()

    if not mi_conexion:
        print("Error de conexión.")
        return None

    cursor = mi_conexion.cursor()

    try:
        sql = """
            SELECT id, nombre, direccion, telefono, correo, rol, fecha_inicio, salario 
            FROM empleado 
            WHERE id = %s
        """
        valores = (id_empleado,)

        cursor.execute(sql, valores)
        resultado = cursor.fetchone()

        if resultado:
            print("Empleado encontrado:", resultado)
            return resultado
        else:
            print("No se encontró ningún empleado con ese ID.")
            return None

    except Exception as e:
        print(f"Error al buscar el empleado: {e}")
        return None

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if mi_conexion:
            mi_conexion.close()


#------------------------------------------------------------------------------

def actualizar_empleado(id_empleado, nombre, direccion, telefono, correo, contrasena, rol, fecha_inicio, salario):
    mi_conexion = conexion()

    if not mi_conexion:
        print("Error de conexión.")
        return False

    cursor = mi_conexion.cursor()

    try:
        sql = """
            UPDATE empleado 
            SET nombre = %s, direccion = %s, telefono = %s, correo = %s, 
                contrasena = %s, rol = %s, fecha_inicio = %s, salario = %s 
            WHERE id = %s
        """
        valores = (nombre, direccion, telefono, correo, contrasena, rol, fecha_inicio, salario, id_empleado)

        cursor.execute(sql, valores)
        mi_conexion.commit()

        if cursor.rowcount > 0:
            print("Empleado actualizado exitosamente.")
            return True
        else:
            print("No se encontró ningún empleado con ese ID.")
            return False

    except Exception as e:
        print(f"Error al actualizar el empleado: {e}")
        return False

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if mi_conexion:
            mi_conexion.close()


#------------------------------------------------------------------------------

def eliminar_empleado(id_empleado):
    mi_conexion = conexion()

    if not mi_conexion:
        print("Error de conexión.")
        return False

    cursor = mi_conexion.cursor()

    try:
        sql = "DELETE FROM empleado WHERE id = %s"
        valores = (id_empleado,)

        cursor.execute(sql, valores)
        mi_conexion.commit()

        if cursor.rowcount > 0:
            print("Empleado eliminado exitosamente.")
            return True
        else:
            print("No se encontró ningún empleado con ese ID para eliminar.")
            return False

    except Exception as e:
        print(f"Error al eliminar el empleado: {e}")
        return False

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if mi_conexion:
            mi_conexion.close()