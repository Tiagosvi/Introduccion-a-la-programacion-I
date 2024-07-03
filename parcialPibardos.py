from queue import Queue as Cola

filaClientes:Cola[(str,str)] = Cola()
filaClientes.put(("Pedro","comun"))
filaClientes.put(("Juan","vip"))
filaClientes.put(("pablo","comun"))
filaClientes.put(("Mariano","vip"))

def reordenar_cola_priorizando_vips (filaClientes: Cola[(str,str)]) -> Cola[str]:
    clientes:list[(int,str)] = []
    res: Cola[str] = Cola()
    des:list[str] = []

    while not Cola.empty (filaClientes):
        clientes.append(filaClientes.get())


    for i in range (len(clientes)):
        if clientes[i][1] == "vip":
            res.put(clientes[i][0])
    
    for i in range (len(clientes)):
        if clientes [i][1] == "comun":
            res.put(clientes[i][0])

#Desarmo para chequear que haya quedado bien:
    while not Cola.empty(res):
        des.append(res.get())

    print(des)

    
reordenar_cola_priorizando_vips (filaClientes)

estrategias: dict[str,str] = {"jugador1":"me la banco y no me desvio","tomas":"me la banco y no me desvio"}
def torneo_de_gallinas (estrategias: dict[str,str]) -> dict[str,int]:
    res:dict[str,int] = {}
    

    for (jugador,estrategia) in estrategias.items():
        puntaje = 0
        for (k,v) in estrategias.items():
            if jugador != k:
                if estrategia  == "me desvio siempre" and v == "me desvio siempre":
                    puntaje-= 10
                elif estrategia == "me la banco y no me desvio" and v == "me la banco y no me desvio":
                    puntaje -= 5
                elif estrategia == "me la banco y no me desvio" and v == "me desvio siempre":
                    puntaje += 10
                else: puntaje -= 15
            res[k] = puntaje

    return res

print(torneo_de_gallinas(estrategias))

def cuantos_sufijos_son_palindromos(texto: str) -> int:
    res:int = 0
    palabra:list[str] = []
    for i in range(len(texto)):
        palabra += ((list(texto))[i])
    
    for j in range (len(palabra)):
        reverso:list[str] = []
        for i in range (len(palabra)-1,-1,-1):
            reverso += palabra [i]

        if palabra == reverso:
            res += 1
        palabra.pop(0)

    return res


def quien_gano_el_tateti_facilito(tablero: list[list[str]]) -> int:
    #res:list[list[str]] = []
    #for i in range (len(tablero)):
     #   columna:list[str] = []
      #  for j in range (len(tablero)):
       #     columna+=tablero[j][i]
        #res.append(columna)

    #print(res)

    contadorX:int = 0
    contadorO:int = 0
    ganoX: bool = False
    ganoY: bool = False

    for i in range (len(tablero)):
        for j in range (len(tablero)):
            if tablero [j][i] == "X":
                contadorX += 1
                contadorO = 0
                if contadorX >= 3:
                    ganoX = True

            elif tablero [j][i] == "O":
                contadorX = 0
                contadorO += 1
                if contadorO >= 3:
                    ganoY = True

            else: 
                contadorX = 0
                contadorO = 0


    res:int = 0
    if ganoX and not ganoY:
        res = 1

    elif ganoY and not ganoX:
        res = 2
    
    elif ganoY and ganoX:
        res = 3

    else: res = 0

    return res


tablero1 =[
     ["X","O","X"," "," "," "," "," "],
     ["X"," "," "," "," "," "," "," "],
     ["O"," "," "," "," ","X"," ","X"],
     ["O"," "," "," "," "," "," ","X"],
     ["O"," ","O"," "," "," "," ","O"],
     [" "," ","X","O"," ","O"," ","O"],
     ["X"," ","O"," ","O"," "," ","O"],
     ["X"," "," "," "," "," "," ","O"]
 ]

print(quien_gano_el_tateti_facilito(tablero1))










                




