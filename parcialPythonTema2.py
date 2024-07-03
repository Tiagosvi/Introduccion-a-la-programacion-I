#Ejercicio 3:

def maximo (tiempos_indice:list[tuple[int,int]]) -> int:
    maximo = tiempos_indice[0]
    for i in range (1,len(tiempos_indice)):
        if tiempos_indice [i][0] > maximo[0]:
            maximo = tiempos_indice[i]

    return maximo[1]

def tiempo_mas_rapido (tiempos_salas: list[int]) -> int:
    tiempos_indice:list[tuple[int,int]] = []
    res:int = 0

    for i in range (len(tiempos_salas)):
        if tiempos_salas [i] <= 60:
            tiempos_indice.append([tiempos_salas[i],i])

    res = maximo(tiempos_indice)
    return res


#tiempos_salas = [50,80,0,55,55,54] 
#print(tiempo_mas_rapido (tiempos_salas))

#Ejercicio 2:
def tiempos_salio (lista:list[int]) -> tuple[int,float]:
    logro_salir: int = 0
    tiempos_salida:int = 0 
    res: tuple[int,int]

    for i in range (len(lista)):
         if lista[i] < 61:
             logro_salir += 1
             tiempos_salida += lista[i]


    if logro_salir != 0:
        res = (logro_salir,(tiempos_salida / logro_salir))
    else: res = (logro_salir,float(0))
    return res
             
             


def promedio_de_salidas (registro: dict[str,list[int]]) -> dict[str,tuple[int,float]]:
    res:dict[str,tuple[int,float]] = {}

    for k,v in registro.items():
        res[k] = tiempos_salio(v)

    return res


registro = {"Juan": [61],"Pablo":[30,40,60]}
print(promedio_de_salidas(registro))


#Ejercicio 3:
def escape_en_solitario (amigos_por_salas:list[list[int]]) -> list[int]:
    res: list[int] = []
    for i in range(len(amigos_por_salas)):
        solo:bool = True
        if amigos_por_salas[i][0] != 0:
                solo: bool = False
        elif amigos_por_salas [i][1] != 0:
                solo:bool = False
        elif amigos_por_salas [i][3] != 0:
                solo:bool = False
        elif amigos_por_salas [i][2] == 0:
                solo:bool = False
            
        if solo:
            res.append(i)

    return res
        

#Ejercicio 4:

def mas_larga (lista_sec:list[tuple[int,int]]) -> tuple[int,int]:
    maximo = lista_sec[0][1] - lista_sec [0][0]
    res:tuple[int,int] = (lista_sec [0][0],lista_sec[0][1])
    for i in range (1,len(lista_sec)):
        if lista_sec[i][1] - lista_sec [i][0] > maximo:
            maximo = lista_sec[i][1] - lista_sec [i][0]
            res = (lista_sec[i][0],lista_sec[i][1])

    return res

        

def racha_mas_larga (tiempos:list[int]) -> tuple[int,int]:
    indice_inicio:int = 0
    indice_final:int = 0
    lista_sec:list[tuple[int,int]] = []
    cantidad:int = 0
    res:tuple[int,int] = ()

    for i in range (len(tiempos)):
        if tiempos[i] == 61:
              lista_sec.append([(indice_final + 1 - cantidad),indice_final - 1])
              cantidad = 0

        else: 
             indice_final = i
             cantidad += 1
        
    lista_sec.append([(indice_final + 1 - cantidad),indice_final])
    print(lista_sec)
    
    res = mas_larga(lista_sec)
    return res


tiempos = [61,61,62,60,4,61]

print(racha_mas_larga(tiempos))
         










amigos_por_salas = [[0,2,5,3],[0,0,0,0]] #-> [0,2]
print(escape_en_solitario(amigos_por_salas))
