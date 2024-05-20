def pertenece (s: list [int], e: int ) -> bool:
    for n in s:
        if e == n:
            return True
    
    return False

print(pertenece([1,2,3],4))

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

