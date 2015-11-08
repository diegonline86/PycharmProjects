__author__ = 'Diego Alberto Silguero'
# -*- coding: utf-8 -*-

def union_listas(lista1 , lista2):
    res = lista1 + lista2
    for n in lista1:
        for k in lista2:
            if(n==k):
                res.remove(n)

    return res

nombres1 = ['Diego','Carlos','Alfonso','José','Javier','Manuel']
nombres2 = ['Diego','Alberto','Francisco','José','Jorge','Manuel']

print(union_listas(nombres1,nombres2))

