import os
import sys

# Agrega la carpeta raíz del proyecto al path de Python
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from DAO.EmpleadoDAO import validacion
from DAO.UsuarioDao import Registro


def mostrar_menu():
  print("==========================")
  print("||   Elija una opcion   ||")
  print("||======================||")
  print("||  1. Iniciar Sesion   ||")
  print("||   2. Registrarse     ||")
  print("==========================")


# 1. Mostramos el menú en pantalla
mostrar_menu()

# 2. Capturamos la opción del usuario
opcion = int(input("Ingrese una opcion: "))

# 3. Evaluamos la opción elegida
if opcion == 1:
  print("\n--- INICIO DE SESIÓN ---")
  correo = input("Ingrese su correo Electronico: ")
  contrasena = input("Ingrese su contraseña: ")

  # 4. Llamamos a la función de validación pasándole los datos ingresados
  es_valido = validacion(correo, contrasena)

  if es_valido:
    print("\n ¡Inicio de sesión exitoso! Bienvenido.")
  else:
    print("\n Error: Correo o contraseña incorrectos.")

elif opcion == 2:
  print("\n--- REGISTRO ---")

  print("Ingrese lo siguientes datos")
  
  nombreRegistro = input("Ingrese su nombre: ")
  direccionRegistro = input("Ingrese su direccion: ")
  telefonoRegistro = input("Ingrese su numero telefonico: ")
  correoRegistro = input("Ingrese su correo: ")

  registro = Registro(nombreRegistro, direccionRegistro, telefonoRegistro, correoRegistro)

  if registro:
    print("Se registro con exito")
  else:
    print("Error!")

else:
  print("\n Opción no válida. Intente nuevamente.")