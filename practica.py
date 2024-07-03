def verificar_transacciones(s:str) -> int:
    saldo:int = 0
    for i in range(len(s)):
        if saldo >= 0:
            if s[i] == 'r':
                saldo += 350
            elif s[i] == "v":
                saldo -= 56
            elif s[i] == "s":
                print(saldo)
            elif s[i] == "x":
                return saldo
        else: return saldo

    return saldo

#print(verificar_transacciones("svx"))

def valor_minimo(s: list[(float, float)]) -> float:
    res:float = s[0][0]
    for i in range(1,len(s)):
        if s[i][0] < res:
            res = s[i][0]

    return res

#s = [(-6, 5.2), (10.4, 15.1), (19.7, 28.9), (-6, 35.6), (2.0, 1.3)]
#print(valor_minimo(s))


def minimo (cotizaciones: list[tuple[int,float]]) -> float:
    min: int = cotizaciones[0][1]
    for i in range(1, len(cotizaciones)):
        if cotizaciones[i][1] < min:
            min = cotizaciones[i][1]
    return min


def maximo (cotizaciones: list[tuple[int,float]]) -> float:
    max: int = cotizaciones[0][1]
    for i in range(1, len(cotizaciones)):
        if cotizaciones[i][1] > max:
            max = cotizaciones[i][1]
    return max



def valores_extremos(cotizaciones_diarias: dict[str, list[tuple[int, float]]]) -> dict[str,tuple[float, float]]:
    res: dict[str,tuple[float,float]] = {}

    for k,v in cotizaciones_diarias.items():
        res[k] = (minimo(v),maximo(v)) 

    return res


cotizaciones_diarias = {"YPF" : [(1,10),(15,111), (31,100)], "ALUA" : [(1,0), (20, 50), (31,30)]}
print(valores_extremos(cotizaciones_diarias))

#def esValido ():

def es_sudoku_valido(m:list[list[int]]) -> bool:
    res: bool = True
    horizontal:list[int] = []
    matriz_invertida: list[list[int]] = []
    columna:list[int] = []

    for i in range (len(m)):
        horizontal = []
        for j in range(len(m)):
            if m[i][j] not in horizontal:
                horizontal.append(m[i][j])
            elif m[i][j] != 0:
                res = False

    for i in range(len(m)):
        for j in range(len(m)):
            columna.append(m[j][i])
        matriz_invertida.append(columna)
        columna = []


    for i in range (len(matriz_invertida)):
        vertical:list[int] = []
        for j in range(len(matriz_invertida)):
            if matriz_invertida[i][j] not in vertical:
                    vertical.append(matriz_invertida[i][j])
            elif matriz_invertida[i][j] != 0:
                res = False

    return res












m = [
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[0, 8, 7, 6, 4, 5, 3, 2, 1],
[0, 0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 4, 0, 0, 0],
[0, 0, 0, 0, 6, 0, 0, 0, 0],
[0, 0, 0, 5, 0, 0, 0, 0, 0], #-> TRUE
[0, 0, 4, 0, 0, 0, 0, 0, 0],
[0, 3, 0, 0, 0, 0, 0, 0, 0],
[2, 0, 0, 0, 0, 0, 0, 0, 0]
]

print(es_sudoku_valido(m))