class Usuario:

    def __init__(self, nombre:str, direccion:str, telefono:str, correo:str):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo


        print("Se a registrado el empleado {} exitosamente".format(nombre))



    #---------------Property/getter-------------------
    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def direccion(self) -> str:
        return self._direccion

    @property
    def telefono(self) -> str:
        return self._telefono

    @property
    def correo(self) -> str:
        return self._correo


    #--------------------------------Setters---------------------------------

    @nombre.setter
    def nombre(self, valor:str) -> None:
        if not valor.strip():
            raise ValueError("El nombre no puede estar vacio")

        self._nombre = valor #Aqui pasa a ser protegido


    @direccion.setter
    def direccion(self, valor:str) -> None:
        if not valor.strip():
            raise ValueError("La direccion no puede estar vacia")

        self._direccion = valor #Aqui pasa a ser protegido


    @telefono.setter
    def telefono(self, valor:str) -> None:
        valor_limpio = valor.strip()

        if not valor_limpio: #Condicion para que el campo no este vacio
            raise ValueError("El campo no puede estar vacio")

        if not valor_limpio.isdigit(): #Condicion para que solo se ingresen digitos
            raise ValueError("El telefono solo puede contener numeros")

        if len(valor_limpio) !=9:  #Condicion para que el telefono no sea maayor a 9
            raise ValueError("El telefono debe tener exactamente 9 digitos")

        self._telefono = valor_limpio #Aqui pasa a ser protegido

    
    @correo.setter
    def correo(self, valor:str):
        valor_limpio = valor.strip()

        if not valor_limpio:
            raise ValueError("El campo no puede estar vacio")

        if "@" not in valor_limpio:
            raise ValueError("El correo debe incluir un '@' ")

        self._correo = valor_limpio #Aqui pasa a ser protegido


    #--------------------------------------Fin del setter----------------------------------------------

def RegistroUsuario():
    try:
        nombre = input("Ingrese su nombre: ")
        direccion = input("Ingrese su dirección: ")
        telefono = input("Ingrese su teléfono: ")
        correo = input("Ingrese su correo: ")

        return Usuario(nombre, direccion, telefono, correo)

    except ValueError as error:
        print(f"Error de validacion{error}")
        return None

if __name__ == "__main__":
    empleado1 = RegistroUsuario()

    if empleado1 is not None:
        print(f"Empleado registrado con exito")
