grado = int(input("De que grado es el polinomio?(primer termino es el de grado mayor): "))
coeficientes = []
for i in range(grado+1):
    coeficientes.append(int(input("Que coeficiente tiene el termino " + str(i+1) + ": ")))
#Una vez ingresados los coeficientes, vamos a ir bajando el grado del polinomio y extrayendo raices mientras sea posible
raices = []
foundit = True
#Tempcoefi es una variable en la que guardaremos temporalmente como nos quedan los coeficientes
tempCoefi = []
divisores = []
while grado > 0 and foundit != False:
    foundit = False
    divisores.clear()
    #Tomamos el ultimo coeficiente, osea el termino independiente
    letdiv = coeficientes[len(coeficientes)-1]
    #Lo volvemos positivo para buscar sus divisores
    if (letdiv < 0): letdiv = -letdiv
    for j in range(letdiv):
        if(letdiv % (j+1) == 0) :
            divisores.append(j+1)
    #Por cada divisor, probamos si podemos aplicar ruffini, en caso de que el final de la cuenta nos de 0 entonces salimos del for
    #y determinamos que ese divisor es raiz
    div = 0
    while foundit == False and div < len(divisores):
        divisor = divisores[div]
        resultado = coeficientes[0]
        tempCoefi.clear()
        i = -1
        while i < 2 and foundit == False:
            for coe in range(len(coeficientes)-1) :
                tempCoefi.append(resultado)
                resultado = (i * divisor * resultado + coeficientes[coe+1])
            if(resultado == 0):
                #Una vez encontrada la raiz, se guardan los coeficientes del ruffini como los coeficientes de verdad para poder ser usados despues
                raices.append(divisor * i)
                coeficientes.clear()
                coeficientes = tempCoefi.copy()
                foundit = True
            else:
                resultado = coeficientes[0]
                tempCoefi.clear()
                i += 2
        div += 1
    #Si luego de recorrer todos los divisores, ninguno nos servia para ruffini, la variable foundit se queda false y el loop termina
    grado -= 1
Polinomio = ""
Raices = ""
for r in raices:
    if(r != 0):
        if(r > 0):
            Raices = Raices + "(x - " + str(r) + ")."
        else:
            Raices = Raices + "(x + " + str(-r) + ")."
Polinomio = Raices + "("
for c in range(len(coeficientes)):
    if(c != len(coeficientes)-1):
        if(len(coeficientes) - (c+1) > 1):
            Polinomio = Polinomio + "(" +  str(coeficientes[c]) + "x^" + str(len(coeficientes) - c) + ") + "
        else:
            Polinomio = Polinomio + "(" + str(coeficientes[c]) + "x) + "
    else:
        Polinomio = Polinomio + "(" + str(coeficientes[c]) + "))"
print("El polinomio queda asi: " + Polinomio)
