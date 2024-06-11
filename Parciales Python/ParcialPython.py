from queue import Queue as Cola

c:Cola = Cola()
c.put(["Tiago","comun"])
c.put(["Juan","vip"])

def reordenar_cola_priorizando_vips(c:Cola[(str,str)]) -> Cola[str]:
    lista:list= []
    res:list = []

    while not (Cola.empty(c)):
        lista.append(c.get())
    
    for i in range (len(lista)):
        if lista[i][1] == "vip":
            c.put(lista[i])
    
    for i in range(len(lista)):
        if lista[i][1] == "comun":
            c.put(lista[i])

    while not (Cola.empty(c)):
        res.append(c.get())

    print(res)
    return res


def torneo_de_gallinas(estrategias: dict[str,str]) -> dict[str,int]:
    contador:int = 0
    res:dict[str,int] = {}
    for (k,v) in estrategias.items():
        puntaje = 0
        for (k2,v2) in estrategias.items():
            if k!=k2:
                if v == "me desvio siempre" and v2 == "me la banco y no me desvio":
                    puntaje -= 15
                if v2 == "me desvio siempre" and v == "me la banco y no me desvio":
                    puntaje += 10
                if v == "me la banco y no me desvio" and v2 == "me la banco y no me desvio":
                    puntaje -= 5
                if v == "me desvio siempre" and v2 == "me desvio siempre":
                    puntaje-= 10
        res[k] = puntaje
    print(res)
    return res

estrategias={
    "Juan":"me la banco y no me desvio",
    "Pedro":"me desvio siempre"
}

def tateti (tablero:list[list[str]]) -> int:
    res:list[list[str]] = []
    columna:list[str] = []
    for j in range (len(tablero)):
        for i in range (len(tablero)):
            columna += tablero[i][j]
        res.append(columna)
        columna = []

    contadorX:int = 0
    contadorY:int = 0
    ganoX = False
    ganoY = False
    for j in range (len(res)):
        for i in range (len(res)):
            if "X" == tablero[i][j]:
                contadorX += 1
                contadorY = 0
                if contadorX >= 3:
                    ganoX:bool = True
                else: ganoX = False
                
            if "O" == tablero [i][j]:
                contadorY += 1
                contadorX = 0
                if contadorY >= 3:
                    ganoY:bool= True
            
            if " " == tablero [i][j]:
                contadorY = 0
                contadorX = 0
                    

 

    if ganoX and ganoY:
        print("trampa")
    elif ganoX:
        print(1)
    elif ganoY:
        print(2)
    else:
        print(0)

tablero = [
    ["O","O"," "," ","X"],
    ["O"," "," "," ","X"],
    ["O","O"," ","X","X"],
    ["X"," "," "," ",""],
    ["X","O"," "," "," "],
]

tateti(tablero)





def palindromo (texto: str) -> bool:
    i:int = 0
    j = len (texto)-1
    while i < len (texto):
        if texto [i] == texto [j]:
            i +=1
            j-=1
        else:
            return False
        
    return True

def sufijos (texto:str) -> int:
    contador:int = 0
    palabra:str = ""
    for i in range (len(texto)-1,-1,-1):
        palabra += texto[i]
        if palindromo(palabra):
            contador += 1

    return contador








