#Consulte un ejemplo donde se implemente la herencia

#aqui se cre la clase
class persona:
    #aqui se construyen los atributos
    def __init__ (self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    #aqui se crea el metodo de presentacion
    def presentacion (self):
        return f"¡Hola! Mi nombre es {self.nombre} y tengo {self.edad} años."
    
#aqui estan las clases derivadas (subclases)
class padre(persona):
    #se agregan los atributos 
    def __init__ (self, nombre, edad, hijos):
        super(). __init__(nombre, edad)
        self.hijos = hijos

    #aqui se crea el metodo trabajo para la clase padre
    def trabajo(self):
        return f"Hola mi es {self.nombre} y estoy trabajando para darle todo a mi familia"
    
#aqui se crea otra clase derivada (subclase)
class madre(persona):
    #aqui se agregan los atributos
    def __init__ (self,  nombre, edad, hijos):
        super().__init__(nombre, edad)
        self.hijos = hijos
    
    #aqui se crea el metodo amaDeCasa para la clase madre
    def amaDeCasa(self):
        return f"Hola mi nombre es {self.nombre} y estoy cuidando mi hogar y a mis hijos"
    
#aqui se crea la clase hijo
class hijo(persona):
    #aqui se agregan los atributos
    def __init__(self, nombre, edad, padres):
        super().__init__(nombre, edad)
        self.padres = padres

    #aqui se crea el metodo estudio para la clase hijo
    def estudio(self):
        return f"¡Hola! mi nombre es {self.nombre} y estoy estudiando para ser profesional en un futuro"
    
#aqui se crean las instancias de las clases
Padre = padre(nombre="Jamir", edad=49, hijos=["Yency", "Kathe"])
Madre = madre(nombre="Maricela", edad=44, hijos=["Yency", "Kathe"])
Hijo1 = hijo(nombre="Yency", edad=18, padres=["Jamir", "Maricela"])
Hijo2 = hijo(nombre="Kathe", edad=23, padres=["Jamir", "Maricela"])

#aqui se acceden a los atributos 
print(padre.presentacion())
print(madre.presentacion())
print(hijo.presentacion())

#aqui se llaman los metodos
print(padre.trabajo())
print(madre.amaDeCasa())
print(hijo.estudio())