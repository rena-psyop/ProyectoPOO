import os
import sys

# Agrega la carpeta raíz del proyecto al path de Python
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from clases.ClaseUsuario import Usuario  # Ajusta si tu archivo tiene otro nombre
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

def crear_usuario(nombre, direccion, telefono, correo):
    mi_conexion = conexion()

    if not mi_conexion:
        print("Error de conexión.")
        return False

    cursor = mi_conexion.cursor()

    try:
        sql = """
            INSERT INTO usuario (nombre, direccion, telefono, correo) 
            VALUES (%s, %s, %s, %s)
        """
        valores = (nombre, direccion, telefono, correo)
        
        cursor.execute(sql, valores)
        mi_conexion.commit()

        print("Usuario creado exitosamente.")
        return True

    except Exception as e:
        print(f"Error al registrar el usuario: {e}")
        return False

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if mi_conexion:
            mi_conexion.close()


#------------------------------------------------------------------------------

def buscar_usuario(id_usuario):
    mi_conexion = conexion()

    if not mi_conexion:
        print("Error de conexión.")
        return None

    cursor = mi_conexion.cursor()

    try:
        # Cambiamos 'usuarios' por 'usuario' (en singular)
        sql = """
            SELECT id, nombre, direccion, telefono, correo 
            FROM usuario 
            WHERE id = %s
        """
        valores = (id_usuario,)

        cursor.execute(sql, valores)
        resultado = cursor.fetchone()

        if resultado:
            print("Usuario encontrado:", resultado)
            return resultado
        else:
            print("No se encontró ningún usuario con ese ID.")
            return None

    except Exception as e:
        print(f"Error al buscar el usuario: {e}")
        return None

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if mi_conexion:
            mi_conexion.close()


#------------------------------------------------------------------------------

def actualizar_usuario(id_usuario, nombre, direccion, telefono, correo):
    mi_conexion = conexion()

    if not mi_conexion:
        print("Error de conexión.")
        return False

    cursor = mi_conexion.cursor()

    try:
        sql = """
            UPDATE usuario 
            SET nombre = %s, direccion = %s, telefono = %s, correo = %s 
            WHERE id = %s
        """
        valores = (nombre, direccion, telefono, correo, id_usuario)

        cursor.execute(sql, valores)
        mi_conexion.commit()

        if cursor.rowcount > 0:
            print("Usuario actualizado exitosamente.")
            return True
        else:
            print("No se encontró ningún usuario con ese ID.")
            return False

    except Exception as e:
        print(f"Error al actualizar el usuario: {e}")
        return False

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if mi_conexion:
            mi_conexion.close()


#------------------------------------------------------------------------------

def eliminar_usuario(id_usuario):
    mi_conexion = conexion()

    if not mi_conexion:
        print("Error de conexión.")
        return False

    cursor = mi_conexion.cursor()

    try:
        sql = "DELETE FROM usuario WHERE id = %s"
        valores = (id_usuario,)

        cursor.execute(sql, valores)
        mi_conexion.commit()

        if cursor.rowcount > 0:
            print("Usuario eliminado exitosamente.")
            return True
        else:
            print("No se encontró ningún usuario con ese ID para eliminar.")
            return False

    except Exception as e:
        print(f"Error al eliminar el usuario: {e}")
        return False

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if mi_conexion:
            mi_conexion.close()