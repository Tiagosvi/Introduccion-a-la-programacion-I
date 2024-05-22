# Ejercicio 1

import math

def imprimir_hola_mundo ():
    print ("Hola Mundo!")

def imprimir_un_verso():
    print ("Llega el domingo voy a ver al campeón \n River vos sos mi locura \n Llevo los trapos para alentarte a vos \n Me chupa un h*evo la yuta \n Yo soy de River porque tenemos aguante \n No como boca son todos vigilantes \n Esta tribuna los noventa minutos \n No para de alentarte…")

def raizDe2():
   c = round(2**0.5, ndigits=4)
   print(c)

def factorial_2() -> float :
    print(math.factorial(2))

def perimetro() -> float:
   print  (2 * math.pi)

#Ejercicio 2

def imprimir_saludo (nombre: str):
    print ("Hola " + nombre)

def raiz_cuadrada_de (numero: int): 
    print (numero**0.5)

def fahrenheit_a_celsius (t: float) -> float:
    res = ((t-32) * 5)/9
    print (res)

def imprimir_dos_veces(estribillo: str):
    print (estribillo * 2) 

def es_multiplo_de (n: float,m: float) -> bool: #Return ya que devuelve un bool
    resultado:bool = True
    if n % m == 0:
        resultado = True
    else:
        resultado = False
    
    return resultado
#resolucion 2 (mas corta):
# resultado:bool = n % m == 0

def es_par (numero: int) -> None: #None ya que no devuelve nada, solo muestra por pantalla
    res:bool = es_multiplo_de(numero,2)
    print (res)

def cantidad_de_pizzas (comensales: float,min_cant_de_porciones: float):
    res = (comensales * min_cant_de_porciones) // 8
    print (res)


#Ejercicio 3
def alguno_es_0 (numero1: float, numero2: float):
    res = (numero1 == 0 and numero2 != 0) or (numero2 == 0 and numero1 != 0)
    print (res)

def ambos_son_0 (numero1: float, numero2: float):
    res = (numero1 == 0 and numero2 == 0)
    print (res) 

def es_nombre_largo (nombre: str) -> bool:
    res = 3 <= len(nombre) <= 8
    print (res)

def es_bisiesto(año: int):
    res = año % 400 == 0 or año % 4 == 0 and año % 100 != 0
    print (res)


#Ejercicio 4


def peso_pino (altura: float):
    if altura >= 3:
        peso = (3 * 100) * 3 + ((altura - 3) * 100) * 2
    else: peso = (altura * 100) * 3

    return peso


def es_peso_util (peso: float) -> bool:
    if 400 < peso < 1000:
        return True
    else:
        return False

def sirve_pino (altura: float) -> bool:
   return es_peso_util (peso_pino (altura))

#Ejercicio 5

def par (numero: int) -> bool:
    if numero % 2 == 0:
        return True
        
def devolver_el_doble_si_es_par (numero: int):
    if par(numero):
        return numero * 2
    else: 
        return numero
    
def devolver_valor_si_es_par_sino_el_que_sigue(numero: int):
    if par(numero):
        return numero
    else:
        return numero + 1
    
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero: int):
    if numero % 9 == 0:
        return numero * 3
    if numero % 3 == 0:
        return numero * 2
    else:
        return numero

def lindo_nombre(nombre: int):
    if len(nombre) >= 5:
        return "Tu nombre tiene muchas letras"
    else:
        return "Tu nombre tiene menos de 5 caracteres"
    
def elRango(numero: int):
    if numero < 5:
        return "Menor a 5"
    if numero > 10 and numero < 20:
        return "Entre 10 y 20"
    if numero > 20:
        return "Mayor a 20"
    else:
        return numero


#Ejercicio 6:

def del_1_al_10():
    x: int = 0
    while x < 11:
        print (x)
        x += 1

def pares_10_al_40():
    x: int = 10
    while x < 41:
        if x % 2 == 0:
            print (x)
            x += 1
        else:
            x += 1

def imprimir_eco():
    i: int = 0
    while i < 11:
        print ("Eco")
        i += 1

def despegue(numero: int):
    i: int = numero
    while i > 0:
        print(i)
        i -= 1

    return ("Despegue")


def viaje_tiempo (partida: int, llegada: int):
    x : int = partida
    y : int = llegada
    while x >= y:
        print (f"Viajó un año al pasado, estamos en el año: {x}")
        x -= 1

    print ("Llegamos")


def viaje_tiempo_Ari (partida: int):
    x: int = partida

    while x >= -384:
        print (f"Viajó un año al pasado, estamos en el año: {x}")
        x -= 20

    print("Llegamos con Ari!!! (Aristoteles)")


#Ejercicio 7:

def del_1_al_10for():
    i : int = 0
    for i in range (11):
        print (i)


def pares_10_al_40for():
    for i in range (10,41):
        if i % 2 == 0: 
         print (i)

def imprimir_ecofor():
    for i in range (11):
        print ("eco")

def despeguefor(numero: int):
    for i in range(numero,0,-1):
        print (i)
    print("Despegue")

def viaje_tiempofor (partida: int, llegada: int):
    for i in range (partida,llegada,-1):
        print (i)
    print ("Llegamos")


def viaje_tiempo_Arifor (partida: int):
    for i in range (partida,-384,-20):
        print (i)
    print ("Llegamos con Ari")

print(viaje_tiempo_Arifor(2024))