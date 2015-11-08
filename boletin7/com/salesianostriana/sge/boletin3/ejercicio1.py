__author__ = 'Diego Alberto Silguero'
# -*- coding: utf-8 -*-

def interseccion_listas(lista1, lista2,):
    res = list()
    for n in lista1:
        for k in lista2:
            if(n==k):
                res.append(n)

    return res


nombres1 = ['Diego','Carlos','Alfonso','José','Javier','Manuel']
nombres2 = ['Diego','Alberto','Francisco','José','Jorge','Manuel']

print(interseccion_listas(nombres1,nombres2))


