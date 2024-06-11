def filtrar_codigos_primos(codigos_barra: list[int]) -> list[int]:
    res:list[int] = []
    k:int = 0
    vuelta:list[int] = []
    numero:int = 0


    for i in range (len(codigos_barra)):
        vuelta.append(codigos_barra[i] % 1000)
    

    for k in range (len(vuelta)):
        esPrimo = True
        for j in range (2, (vuelta[k])):
            if vuelta[k] % j == 0:
                esPrimo = False

        if esPrimo:
            res.append(vuelta[k])

    
    print(res)
    return res

def minimo(conjunto: list[int]) -> int:
    res: float = conjunto[0]
    for i in range(1, (len(conjunto))):
        if conjunto[i] < res:
            res = conjunto[i]
    return res


def maximo(conjunto: list[int]) -> int:
    res: float = conjunto[0]
    for i in range(1, (len(conjunto))):
        if conjunto[i] > res:
            res = conjunto[i]
    return res


def stock_productos(stock_cambios: list[tuple[(str, int)]]) -> dict[str, tuple[(int, int)]]:
    historial_cambios: dict[str, list[int]] = {}
    res: dict[str, tuple[(int, int)]] = {}

    # Agrupa los distintos stocks mediante su nombre (str)
    # Y lo guarda en una lista de ints
    for i in range(len(stock_cambios)):
        producto_nombre: str = stock_cambios[i][0]
        stock_producto: int = stock_cambios[i][1]
        if producto_nombre in historial_cambios.keys():
            historial_cambios[producto_nombre] += [stock_producto]
        else:
            historial_cambios[producto_nombre] = [stock_producto]

    # Por cada clave del diccionario anterior busca el maximo y minimo y lo guarda como tupla en otro diccionario
    lista_claves: list[str] = list(historial_cambios.keys())
    for i in range(len(lista_claves)):
        producto_nombre: str = lista_claves[i]
        historial: list[int] = historial_cambios[producto_nombre]
        res[producto_nombre] = (minimo(historial), maximo(historial))
    return res


a: list[tuple[(str, int)]] = [("marcelo", 2), ("marcelo", 3),
                              ("marcelo", 10), ("conocelo", 1),
                              ("lucas", 20), ("lucas", -100)]
print(stock_productos(a))

#truefalse                              falsefalse                              truetrue                    falsetrue
grilla_horaria:list[list[str]] = [["m","m","m","m","m","p","p","p"],["m","k","k","m","m","p","p","p"],["m","m","m","m","p","p","p","p"],["m","m","m","l","p","p","p","p"],
                                  ["m","m","l","m","n","p","p","p"],["m","m","l","m","n","p","p","p"],["m","m","l","m","n","p","p","p"]]


def ejmalisimo(grilla_horaria:list[list[str]]) -> list[tuple[bool,bool]]:
    res:list[tuple[bool,bool]] = []

    for i in range(len(grilla_horaria)):
        igualesManana:bool = True
        persona:str = ""
        for k in range(0,4,1):
            if persona == "":
                persona = grilla_horaria[i][k] 
            elif persona != grilla_horaria[i][k]:
                igualesManana = False

        igualesTarde:bool = True
        persona:str = ""
        for k in range(4,8,1):
            if persona == "":
                persona = grilla_horaria[i][k] 
            elif persona != grilla_horaria[i][k]:
                igualesTarde = False
        res.append((igualesManana,igualesTarde))

    print(res)

ejmalisimo(grilla_horaria)

