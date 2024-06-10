#ARCHIVOS:

#Ejercicio 1:
def contar_lineas (nombrearchivo : str) -> int:
        f=open(nombrearchivo)
        lineas:list [str] = f.readlines()
        cantidad:int = len(lineas)
        return cantidad

def existe_palabra(palabra : str, nombrearchivo : str) -> bool:
    f=open(nombrearchivo)
    for i in f.readlines():
        if palabra in i:
            return True
    return False

def cantidad_de_apariciones (palabra: str, nombrearchivo: str) -> int:
    f=open(nombrearchivo)
    cantidad:int = 0
    for i in f.readlines():
        if palabra in i:
            cantidad += 1

    return cantidad

#Ejercicio 2:

def clonar_sin_comentarios(nombrearchivo: str):
    f=open(nombrearchivo)
    sincomentarios:list[str] = []
    for linea in f.readlines():
       if not linea[0] ==  "#":
            sincomentarios.append(linea)
    res = open ("sincomentarios"+nombrearchivo, "w")
    res.writelines(sincomentarios)
    res.close()
    f.close()

#hola

#Ejercicio 3:

def reverso(nombrearchivo: str):
    f=open(nombrearchivo)
    lineas = f.readlines ()
    i = len(lineas)-1
    reverso:list[str] = []
    while i > 0:
        reverso.append (lineas [i])
        i-=1
    res = open ("reverso.txt","w")
    res.writelines(reverso)
    res.close()
    f.close()

#Ejercicio 4:

def agregar_frase_al_final(nombrearchivo: str, frase: str):
    f=open(nombrearchivo)
    agregarFinal:list[str] = []
    for linea in f.readlines():
        agregarFinal.append(linea)
    res = open ("agregarFinal","w")
    res.writelines(agregarFinal + [frase])
    res.close()
    f.close()

agregar_frase_al_final("prueba","hola")

#Ejercicio 5:
def agregar_frase_al_principio(nombrearchivo: str, frase: str):
    f=open(nombrearchivo)
    agregarPrincipio:list[str] = []
    for linea in f.readlines():
        agregarPrincipio.append(linea)
    res = open ("agregarPrincipio","w")
    res.writelines([frase] + agregarPrincipio)
    res.close()
    f.close()


#Ejercicio 6:

def listar_palabras_de_archivo (nombrearchivo: str) -> list:
    f=open(nombrearchivo)
    lineas = f.readlines()
    i = 0
    palabras:list[str] = []

    while i < len(lineas):
        if len(lineas [i]) >= 5:
            palabras.append(lineas[i])
            i+=1
        else:
            i+=1

    res=open("palabras","w")
    res.writelines (palabras)
    res.close
    f.close


#Ejercicio 7:

#def promedio_estudiante(nombrearchivo: str, lu: str) -> float:

#def calcular_promedio_por_estudiante(nombre_archivo_notas: str, nombre_archivo_promedio: str):
    #f=open(nombre_archivo_notas)
    #lineas = f.readlines()
    #i = 0
    #promedios:list[str] = []


#PILAS:
from queue import LifoQueue as Pila
import random

#Ejercicio 8:

def generar_nros_al_azar (cantidad: int, desde: int, hasta: int) -> Pila:
    p:Pila = Pila()

    for i in range (cantidad):
        elemento:int = random.randint (desde, hasta)
        p.put(elemento)

p:Pila = Pila()
p.put(1)
p.put(2)
p.put(3)
p.put(4)
p.put(7)
p.put(6)

#Ejercicio 9:

def cantidad_elementos(p: Pila) -> int:
    sumar: int = 0
    lista:list = []

    while not(Pila.empty(p)):
        sumar += 1
        lista.append(p.get())
    

    for i in range (len(lista)-1,-1):
        p.put(lista[i])

    return sumar

#Ejercicio 10:

def buscar_el_maximo(p: Pila[int]) -> int:
    lista:list = []

    while not(Pila.empty(p)):
        lista.append(p.get())

    for i in range (len(lista)-1,-1):
        p.put(lista[i])
    return max(lista)


#Ejercicio 11:

def esta_bien_balanceada(s: str) -> bool:
    p:Pila = Pila()

    for i in range (len(s)-1,-1,-1):
        if s[i] == "(" or s[i] == ")":
            p.put(s[i])
    
    abierto: int = 0
    cerrado: int = 0 
    while not(Pila.empty(p)):
        elemento:str = p.get()
        if elemento == "(":
            abierto += 1
        else:
            cerrado +=1

    if abierto != cerrado:
        return False
    
    else: return True



#Ejercicio 12 (este no lo hice)


#COLAS:
from queue import Queue as Cola

#Ejercicio 13:
def generar_al_azar(cantidad: int, desde: int, hasta: int) -> Cola[int]:
    c:Cola = Cola()

    for i in range (cantidad):
        elemento:int = random.randint(desde, hasta)
        print(elemento)
        c.put(elemento)
    return c

#Ejercicio 14:

def cantidad_elementos(c: Cola) -> int:
    sumar:int = 0
    lista: list = []

    while not (Cola.empty(c)):
        sumar += 1
        lista.append(c.get())

    for i in range(len(lista)):
        c.put(lista[i])

    return sumar


#Ejercicio 15:

def buscar_maximo (c: Cola[int]) -> int:
    lista:list = []
    prueba:list = []

    while not(Cola.empty(c)):
        lista.append(c.get())

    for i in range (len(lista)):
        c.put(lista[i])

    while not(Cola.empty(c)):
        prueba.append(c.get())

    print(prueba)   

    
    return max(lista)


#EJERCICIO 16:

def armar_secuencia_de_bingo() -> Cola[int]:
    c:Cola = Cola()
    elemento: int = 0
    lista:list = []

    for i in range (12):
        elemento = random.randint (0,99)
        c.put(elemento)

    return c




def pertenece_y_pos(x:int,l:list[int]) -> int:
    res:int = -1
    for i in range(len(l)):
        if x == l[i]:
            res = i
        return res

def jugar_carton_de_bingo (carton: list[int], c: Cola[int]) -> int:
    res:int= 0


    while len(carton) != 0:
        bolita:int = c.get()
        print (bolita)
        if bolita in carton:
            carton.pop(pertenece_y_pos(bolita,carton))
            print(f"CARTON = {carton}")
        res+=1
    print(f"res:{res}")
    return res



#Ejercicio 17:



def n_pacientes_urgentes (c:Cola [(int, str, str)]) -> int:
    i:int = 0
    res: int = 0
    lista:list = []
    
    
    while not(Cola.empty(c)):
        lista.append(c.get())

    for i in range (len(lista)):
        if lista[i][0] <= 3:
           res+=1
    print(res)   
    return res

           

c:Cola = Cola()
c.put(["Juan",20,False,True])
c.put(["Pedro",20,True,False])

def atencion_a_clientes(c : Cola[(str, int, bool, bool)]) -> Cola[(str, int, bool, bool)]:
    i:int = 0
    res: int = 0
    lista:list = []
    sol:list = []
    
    while not(Cola.empty(c)):
        lista.append(c.get())

    for i in range (len(lista)):
        if lista[i][2] == True:
            c.put(lista[i])
    
    for i in range (len(lista)):
        if lista[i][3] == True:
            c.put(lista[i])
        
    while not(Cola.empty(c)):
        sol.append(c.get())
    
    print(sol)
    return c



#DICCIONARIOS:

#Ejercicio 19:

def agrupar_por_longitud(palabras: list[str]) -> dict:
    d:dict[int,int] = {}
    
    for i in range (len(palabras)):
        if len(palabras[i]) not in d:
            d[len(palabras[i])] = 1
        else: 
            d[len(palabras[i])] += 1

    print(d)
    return d

#Ejercicio 20:

#def calcular_promedio_por_estudiante(notas: str) -> dict[str,float]: NO ME SALEE!!!
#   d:dict[str, float]

#Ejercicio 21:
palabras: list[str] = ["Hola","Hola","Mundo","Murcielago","chau"]

def la_palabra_mas_frecuente(palabras: list[str]) -> dict:
    d:dict[str,int] = {}
    res:int = 0
    for i in range (len(palabras)):
        if palabras [i] not in d:
            d[palabras[i]] = 1
        else:
            d[palabras[i]] += 1

    
    for i,j in d.items():
        if res < j:
            res= j
            val=i

    print(val)
    return val

la_palabra_mas_frecuente(palabras)

#Ejercicio 22:

historiales:dict[str,Pila[str]] = {}

def visitar_sitio(historiales:dict[str, Pila[str]], usuario:str, sitio:str):
    p:Pila=Pila()
    if usuario not in historiales:
        historiales[usuario] = p.put(sitio)

    else:
        for k,v in historiales.items():
            if k == usuario:
                p.put(sitio)

def navegar_atras(historiales: dict[str, Pila[str]], usuario:str):
    actual:str = ""
    anterior:str = ""

    p = historiales[usuario]
    actual = p.get()
    anterior = p.get()
    p.put(anterior)
    p.put(actual)
    visitar_sitio(historiales,usuario,anterior)


