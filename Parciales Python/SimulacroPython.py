def ultima_aparicion(s: list[int], e:int) -> int:
    i:int = len(s)
    acu: int = 0
    res:int = 0
    
    for i in range(len(s)-1,-1,-1):
        if s[i] == e:
            acu += 1
            res = len(s) - acu
            print(res)
            return res
        else: 
            acu += 1



def elementos_exclusivos(s: list[int], t: list[int]) -> list[int]:
    i:int = 0
    res:list[int] = []

    for i in range (len(s)):
        if s[i] not in t:
            if not s[i] in res:
                res.append(s[i])

    for i in range (len(t)):
        if t[i] not in s:
            if not t[i] in res:
                res.append(t[i])

    print(res)
    return res

s = [-1,4,0,4,3,0,100,0,-1,-1]
t = [0,100,5,0,100,-1,5]

elementos_exclusivos(s,t)

def contar_traducciones_iguales(ing: dict[str,str], ale: dict[str,str]) -> int:

    contador:int=0
    for (k1,v1) in ing.items():
        for (k2,v2) in ale.items():
            if k1==k2 and v1 == v2: 
                contador+=1
    return contador



def convertir_a_diccionario(lista: list[int]) -> dict[int,int]:
    res: dict[int,int] = {}

    for i in range (len(lista)):
        if lista[i] not in res:
            res[lista[i]] = 1
        else:
            res[lista[i]] += 1
    
    print(res)
    return res

convertir_a_diccionario([-1,0,4,100,100,-1,-1])
         


