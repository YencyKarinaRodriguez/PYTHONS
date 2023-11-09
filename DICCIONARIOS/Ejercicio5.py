#Funciones con parametros

#se define la funcion
def raiz(value):
    return value ** (1/2)

#lee el valor de la raiz cuadrada
print(f'La raiz cuadrada es: {raiz(4)}')

def validarsiexiste(obj):
    
    #lee si obj es verdadero
    if obj:
        print(f"{obj} is True")

    #lee si obj es falso    
    else:
        print(f"{obj} is False")

validarsiexiste(1)