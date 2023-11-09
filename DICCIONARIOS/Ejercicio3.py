#Agregar datos al diccionario despues de creado

#Tecnicas de iteracion

#lee las calificaciones
calificaciones1 = {
'nombre': 'Sandra',
'notafinal': 5.0

}

calificaciones2 = {
'Sandra': 5.0,
'Adriana':5.0,
'Mauricio':4.5,
'Jose':2.5

}

#se agregan datos al diccionario

calificaciones2.update({"Rosa": 3.7, "German": 4.8})
for i, j in calificaciones2.items():
    print(i,j)