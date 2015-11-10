# -*- coding: utf-8 -*-


def nombresInicial(listaNombres, letra):
    res = list()
    for nombre in listaNombres:
        if nombre.startswith(letra):
            res.append(nombre)
    return res

listaNombres = ["Diego", "Alvaro", "Alberto", "Antonio", "Carlos", "Rafa","Ricardo"]


print(nombresInicial(listaNombres,"A"))