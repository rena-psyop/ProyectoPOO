import os
import sys

# Agrega la carpeta raíz del proyecto al path de Python
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from DAO.DepartamentoDAO import *
from DAO.EmpleadoDAO import *
from DAO.informeDAO import *
from DAO.proyectoDAO import *
from DAO.RegistroTiempoDAO import *
from DAO.UsuarioDao import *


def MenuMain():
    print("\n" + "=" * 40)
    print("        SISTEMA DE GESTIÓN")
    print("=" * 40)
    print(" [1]  Menú de Departamentos")
    print(" [2]  Menú de Empleados")
    print(" [3]  Menú de Informes")
    print(" [4]  Menú de Proyectos")
    print(" [5]  Menú de Registro de Tiempo")
    print(" [6]  Menú de Usuarios")
    print(" [7]  Salir")
    print("=" * 40)
    
    opcion = input("Seleccione una opción: ")
    return opcion


def MenuDepa():
    print("\n" + "=" * 40)
    print("       MENU DE DEPARTAMENTOS")
    print("=" * 40)
    print(" [1]  Crear Departamento")
    print(" [2]  Buscar Departamento")
    print(" [3]  Modificar Departamento")
    print(" [4]  Eliminar Departamento")
    print(" [5]  Volver al Menú Principal")
    print("=" * 40)
    
    opcion = input("Seleccione una opción: ")
    return opcion


def menu_empleados():
    print("\n" + "=" * 40)
    print("          MENU DE EMPLEADOS")
    print("=" * 40)
    print(" [1]  Crear Empleado")
    print(" [2]  Buscar Empleado")
    print(" [3]  Modificar Empleado")
    print(" [4]  Eliminar Empleado")
    print(" [5]  Volver al Menú Principal")
    print("=" * 40)
    
    opcion = input("Seleccione una opción: ")
    return opcion


def menu_informes():
    print("\n" + "=" * 40)
    print("           MENU DE INFORMES")
    print("=" * 40)
    print(" [1]  Crear Informe")
    print(" [2]  Buscar Informe")
    print(" [3]  Modificar Informe")
    print(" [4]  Eliminar Informe")
    print(" [5]  Volver al Menú Principal")
    print("=" * 40)
    
    opcion = input("Seleccione una opción: ")
    return opcion


def menu_proyectos():
    print("\n" + "=" * 40)
    print("           MENU DE PROYECTOS")
    print("=" * 40)
    print(" [1]  Crear Proyecto")
    print(" [2]  Buscar Proyecto")
    print(" [3]  Modificar Proyecto")
    print(" [4]  Eliminar Proyecto")
    print(" [5]  Volver al Menú Principal")
    print("=" * 40)
    
    opcion = input("Seleccione una opción: ")
    return opcion


def menu_registro_tiempo():
    print("\n" + "=" * 40)
    print("       MENU DE REGISTRO DE TIEMPO")
    print("=" * 40)
    print(" [1]  Registrar Tiempo")
    print(" [2]  Buscar Registro")
    print(" [3]  Modificar Registro")
    print(" [4]  Eliminar Registro")
    print(" [5]  Volver al Menú Principal")
    print("=" * 40)
    
    opcion = input("Seleccione una opción: ")
    return opcion


def menu_usuarios():
    print("\n" + "=" * 40)
    print("           MENU DE USUARIOS")
    print("=" * 40)
    print(" [1]  Crear Usuario")
    print(" [2]  Buscar Usuario")
    print(" [3]  Modificar Usuario")
    print(" [4]  Eliminar Usuario")
    print(" [5]  Volver al Menú Principal")
    print("=" * 40)
    
    opcion = input("Seleccione una opción: ")
    return opcion


# ----------------------------------------------------------
# FUNCIÓN PRINCIPAL (CONTROLADOR DE TODOS LOS MENÚS)
# ----------------------------------------------------------
def main():
    while True:
        opcion_main = MenuMain()

        # 1. MENÚ DEPARTAMENTOS
        if opcion_main == "1":
            while True:
                op_depa = MenuDepa()
                if op_depa == "1":
                    print("\n[Crear Departamento]")
                    nombreDepa = input("Ingrese el nombre del departamento: ")
                    crearDepartamento(nombreDepa)
                elif op_depa == "2":
                    print("\n[Buscar Departamento]")
                    id_departamento = input("Ingrese el ID del departamento a buscar: ")
                    buscarDepartamento(id_departamento)
                elif op_depa == "3":
                    print("\n[Modificar Departamento]")
                    id_departamento = input("Ingrese el ID del departamento a modificar: ")
                    nuevo_nombreDepa = input("Ingrese el nuevo nombre: ")
                    actualizar_departamento(id_departamento, nuevo_nombreDepa)
                elif op_depa == "4":
                    print("\n[Eliminar Departamento]")
                    id_departamento = input("Ingrese el ID del departamento a eliminar: ")
                    eliminar_departamento(id_departamento)
                elif op_depa == "5":
                    break  # Vuelve al Menú Principal
                else:
                    print("\nOpción inválida. Intente nuevamente.")

        # 2. MENÚ EMPLEADOS
        elif opcion_main == "2":
            while True:
                op_emp = menu_empleados()
                if op_emp == "1":
                    print("\n[Crear Empleado]")
                    nombre = input("Ingrese el nombre del empleado: ")
                    direccion = input("Ingrese la dirección: ")
                    telefono = input("Ingrese el teléfono: ")
                    correo = input("Ingrese el correo: ")
                    contrasena = input("Ingrese la contraseña: ")
                    rol = input("Ingrese el rol: ")
                    fecha_inicio = input("Ingrese la fecha de inicio: ")
                    salario = input("Ingrese el salario: ")
                    crear_empleado(nombre, direccion, telefono, correo, contrasena, rol, fecha_inicio, salario)
                elif op_emp == "2":
                    print("\n[Buscar Empleado]")
                    id_empleado = input("Ingrese el ID del empleado a buscar: ")
                    buscar_empleado(id_empleado)
                elif op_emp == "3":
                    print("\n[Modificar Empleado]")
                    id_empleado = input("Ingrese el ID del empleado a modificar: ")
                    nombre = input("Ingrese el nuevo nombre: ")
                    direccion = input("Ingrese la nueva dirección: ")
                    telefono = input("Ingrese el nuevo teléfono: ")
                    correo = input("Ingrese el nuevo correo: ")
                    contrasena = input("Ingrese la nueva contraseña: ")
                    rol = input("Ingrese el nuevo rol: ")
                    fecha_inicio = input("Ingrese la nueva fecha de inicio: ")
                    salario = input("Ingrese el nuevo salario: ")
                    actualizar_empleado(id_empleado, nombre, direccion, telefono, correo, contrasena, rol, fecha_inicio, salario)
                elif op_emp == "4":
                    print("\n[Eliminar Empleado]")
                    id_empleado = input("Ingrese el ID del empleado a eliminar: ")
                    eliminar_empleado(id_empleado)
                elif op_emp == "5":
                    break
                else:
                    print("\nOpción inválida. Intente nuevamente.")

        # 3. MENÚ INFORMES
        elif opcion_main == "3":
            while True:
                op_inf = menu_informes()
                if op_inf == "1":
                    print("\n[Crear Informe]")
                    tipo = input("Ingrese el tipo de informe: ")
                    fecha = input("Ingrese la fecha del informe: ")
                    crear_informe(tipo, fecha)
                elif op_inf == "2":
                    print("\n[Buscar Informe]")
                    id_informe = input("Ingrese el ID del informe a buscar: ")
                    buscar_informe(id_informe)
                elif op_inf == "3":
                    print("\n[Modificar Informe]")
                    id_informe = input("Ingrese el ID del informe a modificar: ")
                    tipo = input("Ingrese el nuevo tipo de informe: ")
                    fecha = input("Ingrese la nueva fecha: ")
                    actualizar_informe(id_informe, tipo, fecha)
                elif op_inf == "4":
                    print("\n[Eliminar Informe]")
                    id_informe = input("Ingrese el ID del informe a eliminar: ")
                    eliminar_informe(id_informe)
                elif op_inf == "5":
                    break
                else:
                    print("\nOpción inválida. Intente nuevamente.")

        # 4. MENÚ PROYECTOS
        elif opcion_main == "4":
            while True:
                op_proy = menu_proyectos()
                if op_proy == "1":
                    print("\n[Crear Proyecto]")
                    nombre_proyecto = input("Ingrese el nombre del proyecto: ")
                    descripcion = input("Ingrese la descripción: ")
                    fecha_inicio_proyecto = input("Ingrese la fecha de inicio del proyecto: ")
                    crear_proyecto(nombre_proyecto, descripcion, fecha_inicio_proyecto)
                elif op_proy == "2":
                    print("\n[Buscar Proyecto]")
                    id_proyecto = input("Ingrese el ID del proyecto a buscar: ")
                    buscar_proyecto(id_proyecto)
                elif op_proy == "3":
                    print("\n[Modificar Proyecto]")
                    id_proyecto = input("Ingrese el ID del proyecto a modificar: ")
                    nombre_proyecto = input("Ingrese el nuevo nombre del proyecto: ")
                    descripcion = input("Ingrese la nueva descripción: ")
                    fecha_inicio_proyecto = input("Ingrese la nueva fecha de inicio del proyecto: ")
                    actualizar_proyecto(id_proyecto, nombre_proyecto, descripcion, fecha_inicio_proyecto)
                elif op_proy == "4":
                    print("\n[Eliminar Proyecto]")
                    id_proyecto = input("Ingrese el ID del proyecto a eliminar: ")
                    eliminar_proyecto(id_proyecto)
                elif op_proy == "5":
                    break
                else:
                    print("\nOpción inválida. Intente nuevamente.")

        # 5. MENÚ REGISTRO DE TIEMPO
        elif opcion_main == "5":
            while True:
                op_reg = menu_registro_tiempo()
                if op_reg == "1":
                    print("\n[Registrar Tiempo]")
                    fecha = input("Ingrese la fecha: ")
                    horas = input("Ingrese la cantidad de horas: ")
                    descripcion = input("Ingrese la descripción: ")
                    crear_registro_tiempo(fecha, horas, descripcion)
                elif op_reg == "2":
                    print("\n[Buscar Registro de Tiempo]")
                    id_registro = input("Ingrese el ID del registro a buscar: ")
                    buscar_registro_tiempo(id_registro)
                elif op_reg == "3":
                    print("\n[Modificar Registro de Tiempo]")
                    id_registro = input("Ingrese el ID del registro a modificar: ")
                    fecha = input("Ingrese la nueva fecha: ")
                    horas = input("Ingrese las nuevas horas: ")
                    descripcion = input("Ingrese la nueva descripción: ")
                    actualizar_registro_tiempo(id_registro, fecha, horas, descripcion)
                elif op_reg == "4":
                    print("\n[Eliminar Registro de Tiempo]")
                    id_registro = input("Ingrese el ID del registro a eliminar: ")
                    eliminar_registro_tiempo(id_registro)
                elif op_reg == "5":
                    break
                else:
                    print("\nOpción inválida. Intente nuevamente.")

        # 6. MENÚ USUARIOS
        elif opcion_main == "6":
            while True:
                op_usu = menu_usuarios()
                if op_usu == "1":
                    print("\n[Crear Usuario]")
                    nombre = input("Ingrese el nombre de usuario: ")
                    direccion = input("Ingrese la dirección: ")
                    telefono = input("Ingrese el teléfono: ")
                    correo = input("Ingrese el correo: ")
                    crear_usuario(nombre, direccion, telefono, correo)
                elif op_usu == "2":
                    print("\n[Buscar Usuario]")
                    id_usuario = input("Ingrese el ID del usuario a buscar: ")
                    buscar_usuario(id_usuario)
                elif op_usu == "3":
                    print("\n[Modificar Usuario]")
                    id_usuario = input("Ingrese el ID del usuario a modificar: ")
                    nombre = input("Ingrese el nuevo nombre: ")
                    direccion = input("Ingrese la nueva dirección: ")
                    telefono = input("Ingrese el nuevo teléfono: ")
                    correo = input("Ingrese el nuevo correo: ")
                    actualizar_usuario(id_usuario, nombre, direccion, telefono, correo)
                elif op_usu == "4":
                    print("\n[Eliminar Usuario]")
                    id_usuario = input("Ingrese el ID del usuario a eliminar: ")
                    eliminar_usuario(id_usuario)
                elif op_usu == "5":
                    break
                else:
                    print("\nOpción inválida. Intente nuevamente.")

        # 7. SALIR (Cerrar sesión y volver a Inicio.py)
        elif opcion_main == "7":
            print("\nCerrando sesión. Volviendo al inicio...")
            import Inicio  # Importación local para evitar errores circulares
            Inicio.iniciar_sesion_sistema()  # Vuelve a desplegar el código de Inicio.py
            return
        else:
            print("\nOpción no válida en el menú principal. Intente nuevamente.")


if __name__ == "__main__":
    main()