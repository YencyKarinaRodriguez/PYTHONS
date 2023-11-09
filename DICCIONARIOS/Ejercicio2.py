#Tecnicas de iterar los diccionarios

print("Técnicas por clave")

for i in calificaciones.keys():
    print(i)

print("Iterar por valor")

for j in calificaciones.values():
    print(j)

nombres = ['Maria', 'Sebastian', 'Ana']
edades = ['18', '25', '30']

for n, e in zip(nombres, edades):
    
    print('Tú nombre es {0} y tu edad {1}.'.format(n, e))