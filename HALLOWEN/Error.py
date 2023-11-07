#listas vacias
aprendiz = []
edad =[]

#se crean las listas ingresando los datos
for i in range(1,31):
    aprendiz.append(input(f"Ingrese el nombre del aprendiz : "))
    edad.append(int(input(f"Ingrese la edad de aprendiz : ")))

#se imprimen las listas
print(f"Lista de aprendices: ")
print(f"Lista de edades: ")

#se muestra el aprendiz que es mayor de edad
mayorDeEdad = edad.index(max(edad))
print(f"Aprendiz con la mayor edad: {aprendiz[mayorDeEdad]}")

#se ingresa el nombre del instructor
nombreInstructor = input("Ingrese el nombre del instructor o de la instructora: ")
aprendiz.insert(1, nombreInstructor)

#se realiza el conteo de los aprendices mayores de edad
aprendizMayorEdad = edad.count(18)
print(f"Cantidad de aprendices con 18 años: {aprendizMayorEdad}")

#se inserta el nombre de un nuevo aprendiz
nomNuevoAprendiz = input("Ingrese el nombre del nuevo aprendiz: ")
aprendiz.append(nomNuevoAprendiz)

#se elimina el nombre del instructor 
aprendiz.remove(nombreInstructor)

#se busca algun dato en la lista 
datoBuscar = input("Ingrese el dato a buscar en la lista de aprendices: ")
if datoBuscar in aprendiz:
    print(f" esta en la lista de aprendices.")
else:
    print(f" no esta en la lista de aprendices.")


# Muestra los primeros 10 aprendices
print(f"Primeros 10 aprendices: {aprendiz[:10]}")

# Muestra los utimos 10 aprendices
print(f"Ultimos 10 aprendices: {aprendiz[-10:]}")

# Muestra del elemento 10 al elemento 20
print(f"Elementos del 10 al 20: {aprendiz[9:19]}")