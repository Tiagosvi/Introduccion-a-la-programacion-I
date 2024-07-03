def apariciones (infeccion:str,registros: list[tuple[int,str]]) -> float:
    cant:int = 0
    for i in range (len(registros)):
        if infeccion == registros[i][1]:
            cant += 1
    return cant

    

def alarma_epidemeologica (registros: list[tuple[int,str]], infecciosas: list[str], umbral:float) -> dict[str,float]:
    res: dict[str,float] = {}

    for i in range(len(infecciosas)):
        if (apariciones(infecciosas[i], registros) / len(registros)) > umbral:
            res[infecciosas[i]] = apariciones(infecciosas[i], registros) / len(registros) * 100
        
    return res

registros = [(50,"fiebre"),(40,"fiebre"),(60,"resfrio")]
infecciosas = ["fiebre","resfrio"]
#print(alarma_epidemeologica(registros,infecciosas,0.3))

def sumar_horas (horas_persona:list[int]) -> int:
    res:int = 0
    for i in range (len(horas_persona)):
        res += horas_persona[i]
    return res

def empleados_del_mes (horas:dict[int,list[int]]) -> list[int]:
    res:list[int] = []
    lista:list[tuple[int,int]] = []

    for k,v in horas.items():
        lista.append([k,sumar_horas(v)])

    maximo:int = lista[0]
    for i in range (1,len(lista)):
        if lista[i][1] > maximo[1]:
            maximo = lista[i]

    res = maximo[0]
    return res

#horas = {}
#print(empleados_del_mes(horas))


def nivel_de_ocupacion (camas_por_piso:list[list[bool]]) -> list[float]:
    res:list[float] = []

    for i in range (len(camas_por_piso)):
        cont:float = 0
        for j in range (len(camas_por_piso[i])):
            if camas_por_piso[i][j] == True:
                cont += 1
        res.append(cont / len(camas_por_piso[i]))

    return res

camas_por_piso = [[True,False,True,True],
                  [False,False,True,False]]
print(nivel_de_ocupacion(camas_por_piso))


from queue import Queue as Cola
def orden_de_atencion (urgentes:Cola[int],postergables:Cola[int]) -> Cola[int]:
    urg:list[int] = []
    pos:list[int] = []
    res:Cola[int] = Cola()
    lista:list[int] =[]
    while not Cola.empty(urgentes):
        urg.append(urgentes.get())

    while not Cola.empty(postergables):
        pos.append(postergables.get())

    for i in range (len(pos)):
        res.put(urg[i])
        res.put(pos[i])

    while not Cola.empty(res):
        lista.append(res.get())

    return lista

postergables = Cola()
postergables.put(4)
postergables.put(5)
urgentes = Cola()
urgentes.put(7)
urgentes.put(2)

print(orden_de_atencion(urgentes,postergables))

    


    






