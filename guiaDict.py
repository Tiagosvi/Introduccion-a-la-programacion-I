def agrupar_por_longitud(palabras: list[str]) -> dict:
    d:dict[int,int] = {}

    for i in range (len(palabras)):
        if len(palabras [i]) not in d:
            d[len(palabras[i])] = 1
        else: 
            d[len(palabras[i])] += 1


    return d

a = "HolacomooestassTiago"
agrupar_por_longitud(a)

def la_palabra_mas_frecuente(palabras: list[str]):
    d:dict[str,int] = {}
    value:int = 0

    for i in range (len(palabras)):
        if (palabras [i]) not in d:
            d[palabras [i]] =  1
        
        else: 
            d[palabras [i]] += 1


    for k,v in d.items():
        if v > value:
            value = v
            key = k

    return key
        


from queue import LifoQueue as Pila

historiales:dict[str,Pila[str]] = {}


def visitar_sitio (historiales:dict[str, Pila[str]], usuario:str, sitio:str):
    p = Pila()
    if usuario not in historiales:
        p.put(sitio)
        historiales[usuario] = p

    for k,v in historiales.items():
        if k == usuario:
            v.put(sitio)


def navegar_atras (historiales: dict[str, Pila[str]], usuario:str):
    p = historiales[usuario]
   
    actual:str = p.get()
    anterior:str = p.get()

    p.put(anterior)
    p.put(actual)
    visitar_sitio(historiales,usuario,anterior)

lista = []
for k,v in historiales.items():
    print(f"Historial de {k}: ")
    while not(Pila.empty(v)):
        lista.append(v.get())

print(lista)


inventario: dict[str,dict[str,int]] = {}

def agregar_producto (inventario: dict[str,dict[str,int]], nombre:str, precio:int, cantidad:int):

    inventario [nombre] = {"precio":precio, "cantidad":cantidad}


def actualizar_stock (inventario: dict[str,dict[str,int]], nombre:str, cantidad:int):

    inventario[nombre]["cantidad"] = cantidad

def actualizar_precios (inventario: dict[str,dict[str,int]], nombre: str, precio:int):

    inventario[nombre]["precio"] = precio

def calcular_valor_inventario (inventario: dict[str,dict[str,int]]) -> float:
    res = 0

    for k,v in inventario.items():
        res += v["precio"] * v["cantidad"]

    return res

agregar_producto(inventario, "gomitas", 50, 3)
agregar_producto(inventario, "caramelos", 25, 10)
actualizar_stock(inventario, "gomitas", 8 )
print(inventario) 
print(calcular_valor_inventario(inventario))
   
