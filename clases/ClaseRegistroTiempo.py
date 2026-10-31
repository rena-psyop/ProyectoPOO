class RegistroTiempo:

    def __init__(self, fecha: str, horas: str, descripcion: str, id: int = None):
        self.__id = id
        self.fecha = fecha
        self.horas = horas
        self.descripcion = descripcion

    #----------------Getter-----------
    @property
    def get_id(self):
        return self.__id

    @property
    def fecha(self) -> str:
        return self._fecha

    @property
    def horas(self) -> str:
        return self._horas

    @property
    def descripcion(self) ->str:
        return self._descripcion

    #----------------Setter-----------

    @fecha.setter
    def fecha(self, valor:str) -> None:
        if not valor.strip():
            raise ValueError("Ingrese una fecha")
        self._fecha = valor #Aqui pasa a ser protegido

    @horas.setter
    def horas(self, valor:str) -> None:
        if not valor.strip():
            raise ValueError("Ingrese las horas trabajadas")
        self._horas = valor #Aqui pasa a ser protegido

    @descripcion.setter
    def descripcion(self, valor:str) -> None:
        if not valor.strip():
            raise ValueError("Ingrese una descripcion")
        self._descripcion = valor #Aqui pasa a ser protegido

    #----------------Fin del setter-----------


def CrearRegistroTiempo() -> RegistroTiempo:
    try:
        fecha = input("Ingrese la fecha: ")
        horas = input("Ingrese las horas trabajadas: ")
        descripcion = input("Ingrese la descripción: ")

        # Al instanciar la clase, tus setters validarán los datos
        return RegistroTiempo(fecha, horas, descripcion)

    except ValueError as error:
        print(f"Error de validacion: {error}")
        return None


if __name__ == "__main__":
    registro1 = CrearRegistroTiempo()

    if registro1 is not None:
        print("Registro de tiempo guardado con exito")