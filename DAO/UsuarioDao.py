import os
import sys

# Agrega la carpeta raíz del proyecto al path de Python
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from clases.ClaseUsuario import Usuario
from conn.conexion import conexion

def Registro(nombreRegistro_Ingresado, direccionRegistro_Ingresado, telefonoRegistro_Ingresado, CorreoRegistro_ingresado):
    # 1. Llamamos a la función UNA SOLA VEZ y guardamos la conexión real
    mi_conexion = conexion()

    if not mi_conexion:
        print("Error de conexión.")
        return False

    try:
        # 2. Usamos la variable 'mi_conexion' (sin paréntesis) para el cursor
        cursor = mi_conexion.cursor()
        
        sql = "INSERT INTO usuario (nombre, direccion, telefono, correo) VALUES (%s, %s, %s, %s)"
        valores = (nombreRegistro_Ingresado, direccionRegistro_Ingresado, telefonoRegistro_Ingresado, CorreoRegistro_ingresado)
        
        cursor.execute(sql, valores)

        # 3. Hacemos el commit SOBRE LA MISMA variable de conexión
        mi_conexion.commit()

        print("¡Usuario registrado con éxito!")
        return True

    except Exception as e:
        print(f"Error al registrar: {e}")
        return False
        
    finally:
        # 4. Buena práctica: cerramos el cursor y la conexión para no saturar la BD
        if 'cursor' in locals() and cursor:
            cursor.close()
        if mi_conexion:
            mi_conexion.close()