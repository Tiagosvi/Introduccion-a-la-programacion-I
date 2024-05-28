def pertenece (s: list [int], e: int ) -> bool:
    for n in s:
        if e == n:
            return True
    
    return False


#Solucion con while pertenece:
#def pertenece2 (s: list [int], e = int ) -> bool:
#   i:int = 0
#   loencontre:bool = False
#    while i < len (s):
#       if e == s[i]:
#           return True
#       else:
#           i+=1

#   if i >= len(s):
#       return False


def divide_a_todos (s: list [int], e: int) -> bool:
    i:int = 0
    while i < len (s):
        if s[i] % e == 0:
            i+=1
        else: 
            return False
        
    return True  
     

def suma_total (s: list[int]) -> int:
    suma: int = 0
    for n in s:
        suma += n #el += acumula

    return suma

#Solucion con While suma:
#   i: int = 0
#    while i < len(s)
#        suma += s[i] #suma = suma + s[i]
#       i += 1
#    
#    return suma


def ordenados (s: list[int])-> bool:
    i:int = 0

    while i < len(s)-1:
        if s[i] < s[i+1]:
          i+=1
        else: 
            return False
        
    return True  


def mayor_a_7 (s: list[str]) -> bool:
    i:int = 0
    while i < len (s):
        if len (s[i]) > 7:
            return True
        else: i+=1

    return False

def palindromo (texto: str) -> bool:
    i:int = 0
    j = len (texto)-1
    while i < len (texto):
        if texto [i] == texto [j]:
            i +=1
            j-=1
        else:
            return False
        
    return True


def fortaleza(contraseña: str) -> str:
    tieneMinuscula : bool = False
    tieneMayuscula : bool = False
    tieneNumero : bool = False
    
    i: int = 0
    while i < len(contraseña):
        if  'a' <= contraseña [i] and contraseña [i] <= 'z':
            tieneMinuscula = True
        if 'A' <= contraseña [i] and contraseña [i] <= 'Z':
            tieneMayuscula = True
        if '0' <= contraseña [i] <= '9':
            tieneNumero = True

        i += 1

    if tieneNumero and tieneMayuscula and tieneMinuscula and len(contraseña) > 8:
        print ("Verde")
    elif len(contraseña) < 5:
        print("Rojo")
    else:
        print ("Amarillo")


def banco (s: list[tuple]) -> int:
    i:int = 0
    plata: int = 0
    while i < len (s):
        if s[i][0] == 'R':
            plata -= s[i][1]

        if s[i][0] == 'I':
            plata += s[i][1]
        
        i+=1
    return plata



def palabra (p: str) -> bool:
    x: int = 0
    cant: int = 0
    while x < len (p):
        if p[x] == 'a':
            cant+=1
        if p[x] == 'e':
            cant+=1
        if p[x] == 'i':
            cant+=1
        if p[x] == 'o':
            cant +=1
        if p[x] == 'u':
            cant +=1
        x += 1

    if cant >= 3:
        return True
    else: return False

    

#Ejercicio 2:

def poner_dos_pares_en_cero (lista: list[int]):
    for i in range (0, len(lista)):
        if i % 2 == 0:
                lista[i] = 0
    return lista
print(poner_dos_pares_en_cero([5,2,4,5]))




#Ejercicio 5

def peretenece_a_cada_uno_v2 (l:list[list[int]],e: int, res: list [bool]):
    res.clear()
    for lista in l:
        res.append(pertenece(lista,e))

