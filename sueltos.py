def nombre_lista (nombre:str, stock_cambios:list[tuple[str,int]]) -> tuple[int,int]:
    acumular:list[int] = []
    res:tuple[int,int] = ()
    for i in range(len(stock_cambios)):
        if stock_cambios[i][0] == nombre:
            acumular.append(stock_cambios[i][1])

    maximo = acumular[0]
    minimo = acumular[0]
    
    for i in range (1,len(acumular)):
        if acumular[i] > maximo:
            maximo = acumular[i]
        elif acumular [i] < minimo:
            minimo = acumular[i]

    res = (minimo,maximo)
    return res

    





def stock_productos (stock_cambios:list[tuple[str,int]]) -> dict[str,tuple[int,int]]:
    res: dict[str,tuple[int,int]] = {}

    for i in range (len(stock_cambios)):
        res[stock_cambios[i][0]] = nombre_lista(stock_cambios[i][0], stock_cambios)

    return res

stock_cambios = [("martillos",4),("pala",2),("martillos",8),("pala",7),("martillos",3)]
print(stock_productos(stock_cambios))

