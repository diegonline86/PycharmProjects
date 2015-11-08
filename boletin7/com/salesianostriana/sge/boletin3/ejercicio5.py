# -*- coding: utf-8 -*-


def cadena_mayor(lista_cadenas):
    res = lista_cadenas[0]
    for cad in lista_cadenas:
        if len(cad)>len(res):
            res = cad

    return res


lista_cadenas = ["perro","pulpo",'aeropuerto','gimnasio','acuario','pez']

print(cadena_mayor(lista_cadenas))
