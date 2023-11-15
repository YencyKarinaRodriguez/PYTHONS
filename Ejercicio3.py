#Consulte un ejemplo donde se implemente el polimorfismo

#aqui se declara la clase 
class persona:
    #aqui se construyen los atributos
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    #aqui se crea el metodo presentacion
    def presentacion(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

#aqui se crea la clase derivada subclase aprendiz
class aprendiz(persona):
    #aqui se crean los atributos
    def __init__(self, nombre, edad, curso):
        super().__init__(nombre, edad)
        self.curso = curso

    #aqui se crea el metodo presentacion
    def presentacion(self):
        return f"Hola, soy {self.nombre}, tengo {self.edad} años y estoy en el curso de {self.curso}."

#aqui se crea la clase derivada subclase instructor
class instructor(persona):
    #aqui se crean los atributos
    def __init__(self, nombre, edad, transversal):
        super().__init__(nombre, edad)
        self.transversal = transversal 

    #aqui se crea el metodo presentacion
    def presentacion(self):
        return f"Hola, soy el/la instructor {self.nombre}, tengo {self.edad} años y enseño {self.transversal}."

#aqui se utiliza la funcion polimorfismo
def saludoPersona(persona):
    print(persona.presentacion())

#aqui se crean las instancias de las clases
Amigo = persona(nombre="Vanessa", edad=19)
Aprendiz = aprendiz(nombre = "Yency", edad = 18, curso = "Tecnologo")
Instructor = instructor(nombre = "Adriana", edad = 45, transversal = "Etica")

#aqui se llama la funcion usando polimorfismo
saludoPersona(Amigo)
saludoPersona(Aprendiz)
saludoPersona(Instructor)
