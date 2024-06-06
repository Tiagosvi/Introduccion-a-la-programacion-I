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



def cantidad_elementos(c: Cola) -> int:
    sumar:int = 0
    lista: list = []

    while not (Cola.empty(c)):
        sumar += 1
        lista.append(c.get())

    for i in range(len(lista)):
        c.put(lista[i])

    return sumar

c:Cola = Cola()
c.put(2)
c.put(3)
c.put(5)
c.put(3)

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

    

print(buscar_maximo(c))




