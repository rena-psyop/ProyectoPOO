import os
import sys

# Agrega la carpeta raíz del proyecto al path de Python
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from clases.ClaseEmpleado import Empleado
from conn.conexion import conexion

# Asegúrate de que tenga los dos parámetros entre paréntesis
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

