#import importa en este caso la libreria de json 
#json es una entidad que acumula valores

import json

computadores = []  #lista vacia

#Creamos las funciones para modificar 

def agregarComputador():
    computador = {} #Datos a pedir al usuario 
    computador["Ambiente"] = input("¿A qué ambiente pertenece?: ")
    computador["ID"] = int(input("Digite el ID del computador: "))
    computador["Cargador"] = input("¿El computador tiene CARGADOR (si)/(no)?: ")
    computador["Mouse"] = input("¿El computador tiene MOUSE (si)/(no)?: ")
    computador["Novedad"] = input("¿Tiene alguna NOVEDAD el computador?: ")
    computadores.append(computador)
                                    #Datos guardadods
def guardarDatos():
    # Convertir la lista a formato json
    datos = json.dumps(computadores, indent=2) #.dumps: es una funcion de json 
                                               #intend: nos permite serializar un objeto Python a un objeto JSON.
    # Guardar en el archivo
    with open('computadores.txt', 'w') as archivo: #open almacena en texto todo lo que emos echo y lo llama 
        archivo.write(datos) #escribe un texto específico en el archivo
    
    print("Sus datos han sido guardados correctamente")

def modificarComputador():
    id_modificar = int(input("Digite el ID del computador que desea modificar (numeros): ")) #Si se encuentra el id va a dar la opcion de seguir
    
    for comp in computadores:
        if comp["ID"] == id_modificar:
            comp["Novedad"] = input("Ingrese la nueva NOVEDAD para el computador: ")
            print("Computador modificado correctamente.")
            return
    
    print("No se encontró ningún computador con ese ID.")  #Si no se encuentra el id no seguira
    

def eliminarComputador(): #Para eliminar la computadora ingresada
    id_eliminar = int(input("Digite el ID del computador que desea eliminar (numeros): "))
    
    for comp in computadores:
        if comp["ID"] == id_eliminar:
            computadores.remove(comp)
            print("Computador eliminado correctamente.")
            return
    
    print("No se encontró ningún computador con ese ID.") #No se va a eliminar  nada porque no se encontro el id

# Main
NumCompu = int(input("¿Cuantos computadores son?: "))

for i in range(NumCompu): 
    agregarComputador()

#Aqui llamamos las funciones 

guardarDatos()

print("Lista de COMPUTADORES:\n", json.dumps(computadores, indent=2)) #Muestra los datos que se ingresaron 

# Modificar un computador
modificarComputador()

# Eliminar un computador
eliminarComputador()

# Mostrar la lista actualizada
print("Lista de COMPUTADORES actualizada:\n", json.dumps(computadores, indent=2)) #Aca sse muestra los cambios guardados 

