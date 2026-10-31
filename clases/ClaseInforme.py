class Informe:

    def __init__(self, tipo: str, fecha: str, id: int = None):
        self.__id = id
        self.tipo = tipo
        self.fecha = fecha

    #----------------Getter-----------

    @property
    def get_id(self):
        return self.__id

    @property
    def tipo(self) -> str:
        return self._tipo

    @property
    def fecha(self) -> str:
        return self._fecha

    #----------------Setter-----------

    @tipo.setter
    def tipo(self, valor:str) -> None:
        if not valor.strip():
            raise ValueError("Ingrese que tipo de informe es")
        self._tipo = valor #Aqui pasa a ser protegido

    @fecha.setter
    def fecha(self, valor:str) -> None:
        if not valor.strip():
            raise ValueError("Ingrese una fecha")
        self._fecha = valor #Aqui pasa a ser protegido

    #----------------Fin del setter-----------

def CrearInforme() -> Informe:
    try:
        tipo = input("Ingrese el tipo de informe: ")
        fecha = input("Ingrese la fecha del informe: ")

        # Al instanciar la clase, los setters ejecutarán la validación
        return Informe(tipo, fecha)

    except ValueError as error:
        print(f"Error de validación: {error}")
        return None


if __name__ == "__main__":
    informe1 = CrearInforme()

    if informe1 is not None:
        print("Informe creado con éxito")