import os
import sys

# Agrega la carpeta raíz del proyecto al path de Python
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from DAO.EmpleadoDAO import validacion
from DAO.UsuarioDao import Registro
from main import main


def mostrar_menu():
    print("\n==========================")
    print("||   Elija una opcion   ||")
    print("||======================||")
    print("||   1. Iniciar Sesion  ||")
    print("||   2. Registrarse     ||")
    print("==========================")


# Bucle principal para mantener el programa corriendo
while True:
    mostrar_menu()

    try:
        opcion = int(input("Ingrese una opcion: "))
    except ValueError:
        print("\n Opción no válida. Por favor, ingrese un número.")
        continue

    # Evaluamos la opción elegida
    if opcion == 1:
        # Bucle específico para repetir el inicio de sesión si hay errores
        while True:
            print("\n--- INICIO DE SESIÓN ---")
            correo = input("Ingrese su correo Electronico: ")
            contrasena = input("Ingrese su contraseña: ")

            # Llamamos a la función de validación pasándole los datos ingresados
            es_valido = validacion(correo, contrasena)

            if es_valido:
                print("\n ¡Inicio de sesión exitoso! Bienvenido.")
                main()  # Ejecuta el menú del sistema
                break   # Al cerrar sesión en el main, rompe este bucle y vuelve al menú principal
            else:
                print("\n Correo o contraseña inválida. Intente nuevamente.")
                # El bucle se repite automáticamente aquí pidiendo los datos otra vez

    elif opcion == 2:
        print("\n--- REGISTRO ---")
        print("Ingrese los siguientes datos:")
        
        nombreRegistro = input("Ingrese su nombre: ")
        direccionRegistro = input("Ingrese su direccion: ")
        telefonoRegistro = input("Ingrese su numero telefonico: ")
        correoRegistro = input("Ingrese su correo: ")

        registro = Registro(nombreRegistro, direccionRegistro, telefonoRegistro, correoRegistro)

        if registro:
            print("\n ¡Se registró con éxito!\n")
        else:
            print("\n Error al registrarse.\n")
        # Vuelve automáticamente al menú principal

    else:
        print("\n Opción no válida. Intente nuevamente.\n")