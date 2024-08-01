def pertenece (e: float, lista: list[float]) -> bool:
    res:bool = False

    for i  in range (len(lista)):
        if lista[i] == e:
            res = True

    return res



def pertenece_a_cada_uno_version_2 (s:list[list[float]], e:float) -> list[bool]: 
    res: list[bool] = []

    for i in range (len(s)):
        if pertenece (e,s[i]):
            res.append(True)
        else: res.append(False)


    return res

s = [[4,5,6,4],
    [3,6,7,9]]



def pertenece_2 (e: float, lista: list[float]) -> bool:
    res: bool = False

    for i  in range (len(lista)):
        if lista[i] >= e:
            res = True

    return res

def pertenece_a_cada_uno_version_1 (s:list[list[float]], e:float) -> list[bool]: 
    res: list[bool] = []

    for i in range (len(s)):
        if pertenece_2 (e,s[i]):
            res.append(True)
        else: res.append(False)


    return res


def es_matriz (s:list[list[float]]) -> bool:
    res:bool = False

    if len(s) > 0 and len(s[0]) > 0:
        res = True

    for i in range (len(s)):
        if res == True:
            res = len(s[i]) == len(s[0])

    return res

from queue import LifoQueue as Pila




def cantidad_elementos (p:Pila) -> int:
    res:int = 0
    lista:list[int] = []

    while not (Pila.empty(p)):
        lista.append(p.get())

    
    for i in range (len(lista)):
        res += 1

    return res

def maximo (lista:list[int]) -> int:
    maximo:int = lista[0]

    for i in range (1, len(lista)):
        if maximo < lista[i]:
            maximo = lista[i]

    return maximo

p:Pila[int] = Pila()
p.put(4)
p.put(7)
p.put(2)
p.put(20)
p.put(5)
p.put(9)

def buscar_el_maximo (p:Pila[int]) -> int:
    res:int = 0
    lista:list[int] = []

    while not (Pila.empty(p)):
        lista.append(p.get())

    res = maximo(lista)
    return res


print(buscar_el_maximo(p))