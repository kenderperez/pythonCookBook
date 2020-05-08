#definicion de la clase
class Usuario:
    
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
        self.especie = 'humano'
    def imprimirNombre(self):
        print(self.nombre)
        
usuario1 = Usuario('kender', 24, 'programador') #instancia de la clase
#ejemlos
usuario1.imprimirNombre()
print(usuario1.especie, usuario1.edad, usuario1.profesion)
