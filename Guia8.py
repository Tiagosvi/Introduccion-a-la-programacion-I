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

def generar_nros_al_azar (cantidad: int, desde: int, hasta: int) -> Pila:
    p:Pila = Pila(maxsize=cantidad)

    for i in range (0, cantidad):
        p.put(random.randint(desde, hasta))

    return p


def generar2(cuantos: int, desde: int, hasta: int) -> Pila:
    p:Pila = generar_nros_al_azar(cuantos, desde, hasta)
    for i in range(0, cuantos):
        p.put(random.randint(desde, hasta))
    while not p.empty():
        print(p.get())

generar2(20,20,80)