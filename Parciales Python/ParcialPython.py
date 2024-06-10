from queue import Queue as Cola

c:Cola = Cola()
c.put(["Tiago","comun"])
c.put(["Juan","vip"])

def reordenar_cola_priorizando_vips(c:Cola[(str,str)]) -> Cola[str]:
    lista:list= []
    res:list = []

    while not (Cola.empty(c)):
        lista.append(c.get())
    
    for i in range (len(lista)):
        if lista[i][1] == "vip":
            c.put(lista[i])
    
    for i in range(len(lista)):
        if lista[i][1] == "comun":
            c.put(lista[i])

    while not (Cola.empty(c)):
        res.append(c.get())

    print(res)
    return res

reordenar_cola_priorizando_vips(c)