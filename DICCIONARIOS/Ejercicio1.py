#Escriba una función en Python que reproduzca lo siguiente:
#𝑓(𝑥, 𝑦) = 𝑥2 + 𝑦2 Valor para X=3 y valor para Y=5

#aqui se define la funcion
def exercise (x,y):
    
    #aqui se escirbe la operacion que pidieron
    result = x*2 + y*2
    
    #aqui se muestra el resultado
    print (f"\nEl resultado de la operacion es de {x} x 2 + {y} x 2 es: {result}")

#aqui se piden los datos para terminar la operacion
exercise (int(input("Digite el valor de x: ")), int(input("Digite el valor de y: ")))