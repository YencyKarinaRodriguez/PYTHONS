#Inventario 

#aqui se declara la clase
class gestorComputadores:
    #aqui se construye el atributo
    def __init__ (self):
        self.computadores = [] #aqui se crea una lista vacia
        
    #aqui se crea el metodo de agregar computador
    def agregarComputador(self):
        comp = {} #aqui se interactua con el usuario para tomar los datos del compu
        comp["Ambiente"] = input("¿A que ambiente pertenece el computador?: ")
        comp["ID"] = int(input("Digite el ID del computador: "))
        comp["Cargador"] = input("¿El computador tiene CARGADOR (si)/(no)?: ")
        comp["Mouse"] = input("¿El computador tiene MOUSE (si)/(no)?: ")
        comp["Novedad"] = input("¿Tiene alguna NOVEDAD el computador?: ")
        self.computadores.append(comp)

    #aqui se crea otro metodo que es para modificar algun dato del computador
    def modificarComputador(self):
        idModificar = int(input("Digite el ID del computador que desea modificar: "))
        for comp in self.computadores:
            if comp["ID"] == idModificar:
                comp["Novedad"] = input("Ingrese la nueva NOVEDAD para el computador: ")
                print("Computador modificado correctamente.")
                return
        print("No se encontro ningun computador con ese ID.")

    #aqui se crea otro metodo que es para elminar algun computador
    def eliminarComputador(self):
        idEliminar = int(input("Digite el ID del computador que desea eliminar: "))
        for comp in self.computadores:
            if comp["ID"] == idEliminar:
                self.computadores.remove(comp)
                print("Computador eliminado correctamente.")
                return
        print("No se encontro ningun computador con ese ID.")

    #aqui impre lo que el usuario digite en la lista creada
    def mostrarLista(self):
        print("Lista de COMPUTADORES:")
        for comp in self.computadores:
            print(f"ID: {comp['ID']}, Ambiente: {comp['Ambiente']}, Cargador: {comp['Cargador']}, Mouse: {comp['Mouse']}, Novedad: {comp['Novedad']}") 

#aqui se llama la clase pirncipal
gestor = gestorComputadores()

numCompu = int(input("¿Cuantos computadores son?: "))

#aqui lee el rango de total de compu para asi agregarlos
for i in range(numCompu): 
    gestor.agregarComputador()

#aqui muestra la lista inicial
gestor.mostrarLista()

#aqui modifica algun computador que el usurio desee
gestor.modificarComputador()

#aqui se elimina el computador que el usuario desee
gestor.eliminarComputador()

#y aqui ya se muestra la lista con los datos ya actualizados
gestor.mostrarLista()



                                #Me voy instru, esto no es para mi... 