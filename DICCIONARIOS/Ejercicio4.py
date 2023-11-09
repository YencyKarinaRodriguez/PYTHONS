#Definir una funcion

#se define la funcion 
def saludar():
    print("saludo")

#retorna un numero
def retornarnumero():
    return 1

saludar()

retornarnumero()

#lee que numero retorna
if retornarnumero()==1:
    print("devolvió un uno")

#lee cuando no se devuelve ningun numero
else:
    print("No devolvió un uno")