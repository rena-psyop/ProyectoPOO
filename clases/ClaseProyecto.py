class Proyecto():

    def __init__(self, nombreProyecto: str, descripcion: str, fecha_inicio_Proyecto: str):
        
        self.nombreProyecto = nombreProyecto
        self.descripcion = descripcion
        self.fecha_inicio_Proyecto = fecha_inicio_Proyecto

    #----------------Getter-----------

    @property
    def nombreProyecto(self) ->str:
        return self._nombreProyecto

    @property
    def descripcion(self) ->str:
        return self._descripcion

    @property
    def fecha_inicio_Proyecto(self) ->str:
        return self._fecha_inicio_Proyecto

    #----------------Setter-----------

    @nombreProyecto.setter
    def nombreProyecto(self, valor:str) -> None:
        if not valor.strip():
            raise ValueError("Debe ingresar un nombre al proyecto")
        self._nombreProyecto = valor #Aqui pasa a ser protegido

    @descripcion.setter
    def descripcion(self, valor:str) -> None:
        if not valor.strip():
            raise ValueError("Ingrese una descripcion del proyecto")
        self._descripcion = valor #Aqui pasa a ser protegido

    @fecha_inicio_Proyecto.setter
    def fecha_inicio_Proyecto(self, valor: str) -> None:
        if not valor.strip():
            raise ValueError("Ingrese la fecha de inicio del proyecto")
        self._fecha_inicio_Proyecto = valor #Aqui pasa a ser protegido

    #----------------Fin del setter-----------

def CrearProyecto() -> Proyecto:
    try:
        nombreProyecto = input("Ingrese el nombre del proyecto: ")
        descripcion = input("Ingrese la descripción del proyecto: ")
        fecha_inicio_Proyecto = input(
            "Ingrese la fecha de inicio del proyecto: "
        )

        # Al instanciar la clase, los setters ejecutarán la validación
        return Proyecto(nombreProyecto, descripcion, fecha_inicio_Proyecto)

    except ValueError as error:
        print(f"Error de validacion: {error}")
        return None


if __name__ == "__main__":
    proyecto1 = CrearProyecto()

    if proyecto1 is not None:
        print("Proyecto creado con exito")