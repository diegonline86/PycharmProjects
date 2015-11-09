# -*- coding: utf-8 -*-


def encriptar(llave,texto):
    res = ""
    for i in range(0,len(texto)):
        res += chr(ord(texto[i])+llave)

    return res

def desencriptar(llave,texto):
    res = ""
    for i in range(0,len(texto)):
        res += chr(ord(texto[i])-llave)

    return res
