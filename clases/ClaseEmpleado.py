import os
import sys

# Agrega la carpeta raíz del proyecto al path de Python
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from clases.ClaseUsuario import Usuario

class Empleado(Usuario):

    def __init__(
        self,
        nombre: str,
        direccion: str,
        telefono: str,
        correo: str,
        contrasena: str,
        rol: str,
        fecha_inicio: str,
        salario: float,
        id: int = None,
    ):
        # Le enviamos a la clase padre Usuario sus 4 atributos requeridos
        super().__init__(nombre, rol, direccion, telefono, correo)

        # Guardamos la contraseña (si es un atributo propio de Empleado) y el resto
        self.id = id
        self.contrasena = contrasena
        self.rol = rol
        self.fecha_inicio = fecha_inicio
        self.salario = salario

    #------------------Property------------------
    @property
    def get_id(self):
        return self.id

    @property
    def rol(self) -> str:
        return self._rol

    @property
    def fecha_inicio(self) ->str:
        return self._fecha_inicio

    @property
    def salario(self) -> float:
        return self._salario


    #--------------------------------Setters---------------------------------

    @rol.setter
    def rol(self, valor:str) -> None:
        if not valor.strip():
            raise ValueError("Ingrese el rol")

        self._rol = valor #Aqui pasa a ser protegido

    
    @fecha_inicio.setter
    def fecha_inicio(self, valor:str) -> None:
        if not valor.strip():
            raise ValueError("Ingrese una fecha")

        self._fecha_inicio = valor #Aqui pasa a ser protegido

    @salario.setter
    def salario(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("El salario debe ser mayor a 0")

        self._salario = valor #Aqui pasa a ser protegido


def CrearEmpleado() -> Empleado:
    try:
        nombre = input("Ingrese su nombre: ")
        direccion = input("Ingrese su dirección: ")
        telefono = input("Ingrese su teléfono: ")
        correo = input("Ingrese su correo: ")
        contrasena = input("Ingrese su contraseña: ")
        rol = input("Ingrese el rol: ")
        fecha_inicio = input("Ingrese la fecha de inicio: ")

        salario_str = input("Ingrese el salario: ")
        salario = float(salario_str)

        return Empleado(
            nombre,
            direccion,
            telefono,
            correo,
            contrasena,
            rol,
            fecha_inicio,
            salario,
        )

    except ValueError as error:
        print(f"Error de validación: {error}")
        return None


if __name__ == "__main__":
    empleado1 = CrearEmpleado()

    if empleado1 is not None:
        print("Empleado registrado con éxito")