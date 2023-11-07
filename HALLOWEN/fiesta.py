# Restricciones
# 1. Mayor de 17
# 2. Pelicula Coco
# 3. Sustancias

#se ingresa el nombre del invitado
nombre = input("Inserte su Nombre: ")

#invitacion y restricciones
print (f"Hola {nombre}\n\nHas sido invitado a mi fiesta de Hallowen\nPara asisitir debes llenar el siguiente formulario\nPero debes cumplir las siguientes restricciones:\n1. Mayor de 17 años\n2. Disfras de la Pelicula Coco\n3. Hora de llegada 8pm\n4. No consumir sustancias psicoactivas.\n")

#se ingresa la edad
edad = int(input(f"{nombre} Inserte su edad: "))

#se valida que sea mayor a 17
if edad >= 17:
    
    #Trajes disponibles en la fiesta
    print("Disfraces de personaje disponibles: Hector, Mama Coco, Ernesto de la cruz o Dante")
    
    #se ingresa el personaje del disfras puesto
    disfras = input(f"{nombre} Inserte el nombre del personaje a disfrazarse: ")
    disfrasMayus = disfras.upper()
    
    #se valida si el disfras el acorde a los requisitos
    if disfrasMayus == "HECTOR" or disfrasMayus == "MAMA COCO" or disfrasMayus == "ERNESTO DE LA CRUZ" or disfrasMayus == "DANTE":
        
        #se confirma si lleva sustaciancias prohibidas
        sustacias = input(F"{nombre} ¿Lleva sustancias psicoactivas? Si/No: ").upper()

        if sustacias == "NO":

            print(f"Bienvenida la fiesta de Hallowen {nombre}")
    
    #si inserto otro personaje no acorde a los requisitos
    else:
        print(f"{nombre} El traje seleccionado no esta disponible")

# si no cumple con el requisito de la edad
else:
    print("No puedes entrar a la fiesta por tu edad")

# disfras = input(f"{nombre} Inserte el nombre del personaje a disfrazarse: ")
# disfrasMayus = disfras.upper()

# disfras == "HECTOR" or disfras == "MAMA COCO" or disfras == "ERNESTO DE LA CRUZ" or disfras == "DANTE":

# print("Inserte otro personaje: Hector, Mama Coco, Ernesto de la cruz o Dante")


# horaLlegada = int(input(f"{nombre} Inserte su hora de llegada: "))

# sustacias = input(F"{nombre} ¿Consume sustacias psicoactivas? Si/No: ")
# sustaciasMayus = sustacias.upper()