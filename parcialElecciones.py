def acomodar (s: list[str]) -> list[str]:
    res: list[str] = []


    for i in range (len(s)):
        if s[i] == "up":
            res.append(s[i])

    for i in range (len(s)):
        if s[i] == "lla":
            res.append(s[i])
    return res

#s = ["up","lla","up","lla","lla"]
#print(acomodar (s))


def pos_umbral (s:list[int],u:int) -> int:
    acumulo: int = 0

    for i in range (len(s)):
        if s[i] > 0:
            acumulo += s[i]
            if acumulo >= u:
                return i
    
    return -1


#s=[2,6,5,2,2]
#print(pos_umbral(s,14))


def cuenta_posiciones_por_nacion (naciones:list[str],torneos:dict[int,list[str]]) -> dict[str,list[int]]:
    res: dict[str,list[int]] = {}

    for i in range (len(naciones)):
        res[naciones[i]] = [0]*len(naciones)

    print(res)

    for k,v in torneos.items():
        for i in range(len(torneos[k])):
            res[torneos[k][i]][i] += 1

    return res


naciones = ["arg", "aus", "nz", "sud"]
torneos = {2023:["nz", "sud", "arg", "aus"], 2022:["nz", "sud", "aus", "arg"]}
print(cuenta_posiciones_por_nacion(naciones,torneos))
