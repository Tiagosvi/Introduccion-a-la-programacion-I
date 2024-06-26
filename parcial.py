def cantidad_de_infecciones(registros: tuple[(int,str)], infeccion: str) -> int:
    res: int = 0
    for _id, _infeccion in registros:
        if _infeccion == infeccion:
            res += 1
    return res

def alarma_epidemiologica (registros: tuple[(int,str)], infecciosas: [str], umbral: float) -> dict[str,float]:

    res: dict[str,float] = {}

    #for i in range(len(infecciosas)):
    #    infecciosas[i]

    for infeccion in infecciosas:
        cantidad_infecciones: int = cantidad_de_infecciones(registros, infeccion)
        if cantidad_infecciones / len(registros) > umbral:
            res[ infeccion ] = cantidad_infecciones / len(registros) * 100

    return res

registros = [(45,"resfrio"),(50,"fiebre"),(20,"resfrio")]
infecciosas = ["resfrio","fiebre"]
print(alarma_epidemiologica(registros,infecciosas, 0.7))

