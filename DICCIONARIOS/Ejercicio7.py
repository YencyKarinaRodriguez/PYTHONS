#Parametros por defecto

def compra(marca,cantidad,valor=2500000):
    return dict(

marca=marca,
cantidad=cantidad,
valor=valor*cantidad

)

print(f' lo comprado fue:{compra("AMD",3)}')