#Consulte un ejemplo donde se declare una clase con atributos y métodos.

#aqui se declara la clase
class persona:

    #aqui se construyen los atributos
    def __init__ (self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    #aqui se crea el metodo para el saludo
    def saludo (self):
        #aqui se define el mensaje a leer y tambien los atributos nombre, edad y ciudad
        print (f"Hola, mi nombres es {self.nombre}, tengo {self.edad} años y soy de {self.ciudad}.")

    #aqui se incrementa la edad
    def incrementarEdad (self, incremento):
        self.edad += incremento
        #aqui se lee el mensaje con la edad incrementada
        print (f"¡Felicidades! Ahora tengo {self.edad} años.")

#aqui se crea una instancia a la clase (persona)
persona1 = persona(nombre = "Tatis", edad = 11, ciudad = "Ibague")

#aqui se accede a los atributos 
print(f"Nombre: {persona1.nombre}")
print(f"Edad: {persona1.edad}")
print(f"Ciudad: {persona1.ciudad}")

#aqui se llaman los metodos
persona1.saludo()
persona1.incrementarEdad(2)
persona1.saludo()