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


def agregar_frase_al_final(nombrearchivo: str, frase: str):
    f=open(nombrearchivo)
    lineas = f.readlines ()
    i:int = 0
    agregarFinal:list[str] = []
    
    while i > 0:
        agregarFinal.append(lineas[i])
        i+=1
    agregarFinal = agregarFinal + frase
    res = open ("agregarFinal","w")
    res.writelines(agregarFinal)
    res.close()
    f.close()

