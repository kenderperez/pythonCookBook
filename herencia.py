class Mascota:
    def __init__(this, nombre, comidaFav):
        this.nombre = nombre
        this.comidaFav = comidaFav
       
    def comer(this):
        print(this.nombre + ' comio ' + this.comidaFav)
    
    def hablar(this):
        print(this.nombre + ' hace ' + this.sonido)
#la clase gato hereda el metodo comer de mascota asi como tambien la propiedad nombre y comidafav
class Gato(Mascota):
    sonido = 'miau!!'
    def cazarRatones(this):
        print(this.nombre + ' atrapo un raton')
    
#la clase perro hereda el metodo comer de mascota asi como tambien la propiedad nombre y comidafav     
class Perro(Mascota):
    sonido = 'guau!!'

        
misu = Gato('felix', 'pescado')
pluto = Perro('pluto', 'huesos')

print(pluto.comer())
print(pluto.hablar())

print(misu.cazarRatones())
print(misu.comer())
print(misu.hablar())

