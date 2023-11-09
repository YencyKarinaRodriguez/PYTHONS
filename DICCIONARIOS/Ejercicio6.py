#Funciones con parametros pocisionales
#se define la funcion
def compra(marca,cantidad,valor):
    return dict(

#aqui muestra que el valor tiene que ser el mismo al requerido ej: cantidad que lleve una cantidad y no otra cosa
marca=marca,
cantidad=cantidad,
valor=valor*cantidad

)

#lee el mensaje de los detalles de la compra
print(f' lo comprado fue:{compra("AMD",3,2500000)}')


#Funciones con parametros nominales
def compra(marca,cantidad,valor):
    return dict(

marca=marca,
cantidad=cantidad,
valor=valor*cantidad

)

print(f' lo comprado fue:{compra("marca=“AMD",cantidad=3,valor=2500000)}')
