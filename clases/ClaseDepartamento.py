import os
import sys

# Agrega la carpeta raíz del proyecto al path de Python
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from clases.ClaseEmpleado import *

class Departamento():
    def __init__(self, nombreDepa: str, id: int = None):
        self.__id = id
        self.nombreDepa = nombreDepa

    #----------------Getter-----------

    @property
    def get_id(self):
        return self.__id

    @property
    def nombreDepa(self) -> str:
        return self._nombreDepa

    #---------------Setter------------

    @nombreDepa.setter
    def nombreDepa(self, valor:str) -> None:
        if not valor.strip():
            raise ValueError("El nombre del departamento no puede estar vacio")

        self._nombreDepa = valor #Aqui pasa a ser protegido

def CrearDepartamento() -> Departamento:
    try:
        nombre_depa = input("Ingrese el nombre del departamento: ")
        return Departamento(nombre_depa)

    except ValueError as error:
        print(f"Error de validación: {error}")
        return None


if __name__ == "__main__":
    depa1 = CrearDepartamento()

    if depa1 is not None:
        print("Departamento creado con éxito.")

def CrearDepartamento() -> Departamento:
    try:
        nombre_depa = input("Ingrese el nombre del departamento: ")
        return Departamento(nombre_depa)

    except ValueError as error:
        print(f"Error de validación: {error}")
        return None


if __name__ == "__main__":
    depa1 = CrearDepartamento()

    if depa1 is not None:
        print("Departamento creado con éxito.")