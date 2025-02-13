class Estudiante:
    def __init__(self, dni:str ,nombre: str, edad: int, ):
        self.__dni = dni
        self.nombre = nombre
        self.edad = edad
        self.activo = True
    
    def get_dni(self) ->str:
        return self.__dni

    def __str__(self) -> str:
        return f"{self.__dni} | {self.nombre}"
    
class Usuario(Estudiante):
    def __init__(self, dni, nombre, edad, username: str, password: str):
        super().__init__(dni, nombre, edad)
        self.username = username
        self.__password = password
        
    def get_password(self) -> str:
        return self.__password
    
    def __str__(self):
        return f"{self.username} | {super().__str__()}"
    
usuario_1 = Usuario("1801200802026", "Javier", 17, "userabc", "abdcefghijklmnopqrstuvwxyz")
print (usuario_1)