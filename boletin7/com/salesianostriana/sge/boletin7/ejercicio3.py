__author__ = 'Diego Alberto Silguero'
# -*- coding: utf-8 -*-


def diferencia_listas(lista1 , lista2):
    for n in lista1:
        for k in lista2:
            if(n==k):
                lista1.remove(n)

    return lista1

nombres1 = ['Diego','Carlos','Alfonso','José','Javier','Manuel']
nombres2 = ['Diego','Alberto','Francisco','José','Jorge','Manuel']

print(diferencia_listas(nombres1,nombres2))