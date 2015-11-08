__author__ = 'Diego Alberto Silguero'
# -*- coding: utf-8 -*-

class Nota():
    def __init__(self,asunto):
        self.__asunto = asunto

    @property
    def asunto(self):
        return self.__asunto

    @asunto.setter
    def asunto(self, asunto):
        self.__asunto = asunto

    def __str__(self):
        return self.__asunto


def menu_agenda():
    agenda = list()
    opcion = -1

    while (opcion!=0):
        opcion= int(input("\nAGENDA ELECTRÓNICA\n"
              "1. Agregar nota\n"
              "2. Borrar nota\n"
              "3. Mostrar una nota\n"
              "4. Mostrar todas las notas\n"
              "0. Salir\n\n"
              "Elige opcion: "))

        if(opcion == 1):
            nota = input("Escribe tu nota: ")
            agenda.append(Nota(nota))
        elif(opcion == 2):
            n = int(input("Introduce número de nota: "))
            if(n<1 or n>len(agenda)):
                print("ERROR. El número de nota no existe")
            else:
                agenda.remove(agenda[n-1])
        elif(opcion == 3):
            n = int(input("Introduce número de nota: "))
            if(n<1 or n>len(agenda)):
                print("ERROR. El número de nota no existe")
            else:
                print(n," - ",agenda[n-1])
        elif(opcion == 4):
            id = 1
            print("\nNOTAS GUARDADAS")
            for nota in agenda:
                print(id," - ",nota)
                id += 1

menu_agenda()







