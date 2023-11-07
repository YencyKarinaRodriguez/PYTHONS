#Tomé el presente ejercicio, y pasé a la función la lista con los días de la semana restantes

#aqui se define la funcion
#week = semana
def list (dia, week = []):

    #aqui se agrega el dia digitado
    week.append(dia)

    #aqui se muestra la lista de la semana
    print (week)

#aqui se agrega el domingo al dia y a la lista de los otros dias
list ("Domingo", ["Lunes", "Martes", "Mieercoles", "Jueves", "Viernes", "Sabado"])