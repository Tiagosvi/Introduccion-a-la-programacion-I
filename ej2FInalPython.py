def buscarPosicion (a:int,s2:list[int]) -> list[int]:
    res:list[int] = []
    for i in range (len(s2)):
        if a > 0:
            res.append(s2[i])
            a -= 1
    return res

def maximo (s:list[int]) -> int:
    maximo:int = s[0]

    for i in range (1,len(s)):
        if s[i] > maximo:
            maximo = s[i]
    return maximo


def problemaFinal (s:list[int], s2:list[int]) -> list[int]:
    res:list[int] = []

    for i in range (len(s)):
       res.append(maximo(buscarPosicion(s[i] + 1,s2)))
    return res
       

s = [4,3,2,9,7]
s2 = [1,2,3,4,5]        
print(problemaFinal(s,s2))

    

