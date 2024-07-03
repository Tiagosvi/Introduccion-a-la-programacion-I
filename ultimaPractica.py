def cantidad_promedio (escape: list[int]) -> tuple[int,float]:
    res: tuple[int,float] = ()
    cantidad_escapes: int = 0
    acumular_tiempo:int = 0
    for i in range (len(escape)):
        if escape [i] < 61:
            cantidad_escapes += 1
            acumular_tiempo += escape[i]

    if cantidad_escapes != 0:
        res = (cantidad_escapes,acumular_tiempo / cantidad_escapes)
    else: res = (0,float(0))

    return res




def promedio_de_salidas (registro: dict[str,list[int]]) -> dict[str,tuple[int,float]]:
    res:dict[str,tuple[int,float]] = {}

    for k,v in registro.items():
        res[k] = cantidad_promedio(v)

    return res

registro = {"Tiago":[50,40,61,70,20],"Gaspi":[30,10,61,50],"Pablo":[70,80]}
print(promedio_de_salidas(registro))