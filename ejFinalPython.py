def cantidadApariciones (n:int, lista: list[int]) -> int:
    res: int = 0

    for i in range (len(lista)):
        if n == lista[i]:
            res += 1

    return res


def esValido (fila:list[int]) -> bool:
    res:bool = True

    for i in range (len(fila)):
        if fila[i] != 0:
            if cantidadApariciones (fila[i],fila) > 1:
                res = False

    return res



def esSodokuValido (tablero:list[list[int]]) -> bool:
    res:bool = True

    for i in range (len(tablero)):
        if esValido(tablero [i]) == False:
            res = False

#Ahora la transpuesta!

    invertida: list[list[int]] = []
    columna:list[int] = []

    for i in range (len(tablero)):
        for j in range (len(tablero)):
            columna.append(tablero[j][i])
        invertida.append(columna)
        columna = []
    
    for i in range (len(invertida)):
        if esValido(invertida[i]) == False:
            res = False

    return res



tablero = [[2,6,5,8,0,0],
           [2,5,7,8]]
print(esSodokuValido(tablero))