from queue import Queue as Cola

#Ejercicio:
def cantidad_de_infecciones(registros: tuple[(int,str)], infeccion: str) -> int:
    res: int = 0
    for _id, _infeccion in registros:
        if _infeccion == infeccion:
            res += 1
    return res

def alarma_epidemiologica (registros: tuple[(int,str)], infecciosas: [str], umbral: float) -> dict[str,float]:

    res: dict[str,float] = {}

    #for i in range(len(infecciosas)):
    #    infecciosas[i]

    for infeccion in infecciosas:
        cantidad_infecciones: int = cantidad_de_infecciones(registros, infeccion)
        if cantidad_infecciones / len(registros) > umbral:
            res[ infeccion ] = cantidad_infecciones / len(registros) * 100

    return res

registros = [(45,"resfrio"),(50,"fiebre"),(20,"resfrio")]
infecciosas = ["resfrio","fiebre"]
print(alarma_epidemiologica(registros,infecciosas, 0.7))


#Ejercicio 2:

urgentes = Cola()
postergables = Cola()
urgentes.put(35)
urgentes.put(50)
urgentes.put(75)
postergables.put(40)
postergables.put(90)
postergables.put(20)



def orden_de_atencion (urgentes: Cola[int], postergables: Cola[int]) -> Cola[int]:
    urg:list[int] = []
    post: list[int] = []
    res = Cola()
    des:list[int] = []

    while not Cola.empty(urgentes):
        urg.append(urgentes.get())

    while not Cola.empty (postergables):
        post.append(postergables.get())

    
    for i in range (len(post)):
        res.put(urg[i])
        res.put(post[i])

#desarmo la cola para ver si quedo

    while not Cola.empty(res):
        des.append(res.get())

    print(des)
    return des

#Ejercicio 3:

def piso (camas_piso: list[bool]) -> float:
    camas_ocupadas:int = 0
    for i in range (len(camas_piso)):
        if camas_piso [i] == True:
            camas_ocupadas += 1

    res = camas_ocupadas / len(camas_piso)
    return res




def nivel_de_ocupacion (camas_por_piso: list[list[bool]]) ->  list[float]:
    res: list[float] = []


    for i in range (len(camas_por_piso)):
            res.append(piso(camas_por_piso[i]))
    return res


camas_por_piso = [ [True,False,True,True],
                   [False,False,True,True],
                   [False,False,False,False] ]
                                           

#Ejercicio 4:

def horas_totales (tiempo: list[int]) -> int:
    h:int = 0

    for i in range (len(tiempo)):
        h += tiempo[i]

    return h

def empleados_del_mes(horas:dict[int,list[int]]) -> list[int]:
    dictAux: dict[int,int] = {}
    comparar = 0
    res:list[int] = []

    for k,v in horas.items():
        dictAux[k] = horas_totales(v)


    for k,v in dictAux.items():
        aux:int = v
        if aux > comparar:
            comparar = aux
            res = []
            res.append(k)
        elif aux == comparar:
            res.append(k)

    return res

        
        

horas = {20:[45],30:[8,45]}
print(empleados_del_mes (horas))
        
