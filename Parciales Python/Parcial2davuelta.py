def acomodar (s: list[str]) -> list[str]:
    i:int = 0
    res:list[str] = []

    for i in range (len(s)):
        if s[i] == "UP":
            res.append(s[i])
    
    for i in range(len(s)):
        if s[i] == "LLA":
            res.append(s[i])


    print (res)
    return res 



def pos_umbral (s: list[int], u:int) -> int:
    i:int = 0
    pos:int = -1
    acumular:int = 0

    while i < len(s):
        if acumular < u:
            if s[i] > 0:
                acumular += s[i]
                i += 1
                pos += 1
            else:
                i += 1
                pos+=1
        else: 
            print(pos)
            return (pos)
    print(-1)        


    

s = [1,-2,0,8,2,3]
u = 9
pos_umbral(s,u)
    
def cuenta_posiciones_por_nacion(naciones: list[str], torneos: dict[int,list[str]]) -> dict[str,list[int]]:
    res:dict[str,list[int]] = {}
    for nacion in naciones:
        res[nacion] = [0]*len(naciones)

    for anio in torneos.keys():
        for i in range(len(torneos[anio])):
            res[torneos[anio][i]][i] += 1
    return res
    

            



