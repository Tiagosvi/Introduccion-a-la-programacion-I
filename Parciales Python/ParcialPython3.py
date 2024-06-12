def verificar_transacciones(s:str) -> int:
    monedero:int = 0

    for i in range (len(s)):
        if s[i] == "v":
            monedero -= 56
        
        if s[i] == "r":
            monedero += 350
        
        if s[i] == "s":
            print(f"saldo:{monedero}")

        if s[i] == "x":
            print(monedero)
            return monedero

        if monedero < 0:
            print (monedero)
            return monedero

    print (monedero) 
    return monedero


def valor_minimo(s:list[tuple[(int, int)]]) -> int:
    res: int = s[0][0]
    for i in range (1,len(s)):
        if s[i][0] < res:
            res = s[i][0]
    print(res)


valor_minimo([(20,40),(9,8)])


def valores_extremos(cotizaciones_diarias: dict[str,list[tuple[int,float]]]) -> dict[str,tuple[float,float]]:
    res:dict[str,tuple[float,float]] = {}
    
    for k,v in cotizaciones_diarias.items():
        mayor:float = v[0][1]
        menor:float = v[0][1]
        for i in range(len(v)):
            if v[i][1] >= mayor:
                mayor = v[i][1]
            elif v[i][1] <= menor:
                menor = v[i][1]
            res[k] = (menor,mayor)
        
    print(res)
    return res

a = {"mochilas":[(20,20),(9,9),(3,4)],"valijas":[(30,30)]}

valores_extremos(a)

def es_sodoku_valido(m:list[list[int]]) -> bool:
    numero: int = 0
    esValido = True
    columna: list[int] = []
    invertida: list[list[int]] = []
    objetosEncontrados: list[int] = []

    for i in range (len(m)):
        objetosEncontrados = []
        for j in range (len(m)):
            if m[i][j] != 0:
                if m[i][j] not in objetosEncontrados:
                    objetosEncontrados.append(m[i][j])
                else: esValido = False
        
    for i in range (len(m)):
        for j in range (len(m)):
            columna += [m[j][i]]
        invertida.append(columna)
        columna = []

    for i in range (len(invertida)):
        objetosEncontrados = []
        for j in range (len(invertida)):
            if invertida[i][j] != 0:
                if invertida[i][j] not in objetosEncontrados:
                    objetosEncontrados.append(invertida[i][j])
                else: esValido = False
        

    print (esValido)


m = [
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[9, 8, 7, 6, 4, 5, 3, 2, 1],
[0, 0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 4, 0, 0, 0],
[0, 0, 0, 0, 6, 0, 0, 0, 0],
[0, 0, 0, 5, 0, 0, 0, 0, 0],
[0, 0, 4, 0, 0, 0, 0, 0, 0],
[0, 3, 0, 0, 0, 0, 0, 0, 0],
[2, 0, 0, 0, 0, 0, 0, 0, 0]
]

es_sodoku_valido(m)

            
            
