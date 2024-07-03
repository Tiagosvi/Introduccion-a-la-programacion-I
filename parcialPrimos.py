def filtrar_codigos_primos (codigos_barra: list[int]) -> list[int]:
    digitos:list[int] = []
    res: list[int] = []
    

    for i in range(len(codigos_barra)):
        digitos.append(codigos_barra [i] % 1000)

    for i in range (len(digitos)):
        esPrimo = True
        for k in range(2,(digitos[i])):
            if digitos [i] % k == 0:
                esPrimo = False
        if esPrimo:
            res.append(digitos[i])

    return res
        

        
codigos_barra = [2101,2103,340,30107]
print(filtrar_codigos_primos(codigos_barra))


def minimo (cantidad:list[int]) -> int:
    minimo = cantidad[0]
    for i in range (1,len(cantidad)):
        if cantidad[i] < minimo:
            minimo = cantidad[i]

    return minimo

def maximo (cantidad:list[int]) -> int:
    maximo = cantidad[0]
    for i in range (1,len(cantidad)):
        if cantidad [i] >= maximo:
            maximo = cantidad[i]

    return maximo

def stock_productos (stock_cambios:list[tuple[(str,int)]]) -> dict[str,tuple[int,int]]: 
    res:dict [str,tuple[int,int]] = {}
    dictAux:dict[str,list[int]] = {}
    lista:list[int] = []


    for i in range (len(stock_cambios)):
        if stock_cambios [i][0] not in dictAux:
            dictAux[stock_cambios[i][0]] = [stock_cambios[i][1]]
        else: 
            dictAux[stock_cambios[i][0]] += [stock_cambios[i][1]]


    lista_claves: list[str] = list(dictAux.keys())
    for i in range(len(lista_claves)):
        historial:list[int] = dictAux[lista_claves[i]]
        res[lista_claves[i]] = (minimo(historial),maximo(historial))
    return res



stock_cambios = [("oro",20),("plata",30),("oro",40),("plata",20)]
print(stock_productos (stock_cambios))

#truefalse                              falsefalse                              truetrue                    falsetrue
grilla_horaria:list[list[str]] = [["m","m","m","m","m","p","p","p"],["m","k","k","m","m","p","p","p"],["m","m","m","m","p","p","p","p"],["m","m","m","l","p","p","p","p"],
                                  ["m","m","l","m","n","p","p","p"],["m","m","o","m","p","p","p","p"],["m","m","l","m","n","p","p","p"]]

def un_resposable_por_turno (grilla_horaria: list[list[str]]) -> list[tuple[(bool,bool)]]:
    res:list[tuple[(bool),(bool)]] =[]
    
    for i in range (len(grilla_horaria)):
        sonIgualesmañana = True
        sonIgualestarde = True
        comparo = grilla_horaria[i][0]
        for j in range (0,4,1):
            if grilla_horaria [i][j] != comparo:
                sonIgualesmañana = False

        comparo = grilla_horaria[i][4]
        for k in range(4,7,1):
            if grilla_horaria[i][k] != comparo:
                sonIgualestarde = False

        res.append((sonIgualesmañana,sonIgualestarde))
    return res

print(un_resposable_por_turno(grilla_horaria))


def subsecuencia_mas_larga(mascotas: list[str]) -> int:
    cant_animal_mayor:int = 0
    cant_animal_actual:int = 0
    posicion_inicial_actual:int = -1
    posicion_inicial_mas_larga:int = -1
    
    for pos_animal in range(len(mascotas)):
        animal: str = mascotas[pos_animal]
        if (animal == "perro" or animal == "gato"):
            if cant_animal_actual == 0:                 # si arranca una nueva subsecuencia
                posicion_inicial_actual = pos_animal    # guardo la posición inicial  
            cant_animal_actual += 1
        else:
            # si no es perro o gato, reset y veo actualizo maximos
            if (cant_animal_actual > cant_animal_mayor):
                cant_animal_mayor = cant_animal_actual
                posicion_inicial_mas_larga = posicion_inicial_actual

            cant_animal_actual = 0
            posicion_inicial_actual = -1
            
        if (cant_animal_actual > cant_animal_mayor):
            posicion_inicial_mas_larga = posicion_inicial_actual
    return posicion_inicial_mas_larga


            

           
    
