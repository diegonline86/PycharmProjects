__author__ = 'Diego Alberto Silguero'
# -*- coding: utf-8 -*-

class Cliente():
    def __init__(self, dni, nombre, apellidos):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellidos = apellidos

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        self.__dni = dni

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, apellidos):
        self.__apellidos = apellidos

    def __str__(self):
        return self.__dni+" - "+self.__apellidos+", "+self.__nombre

class Habitacion():

    def __init__(self, num_hab, reservada, cliente):
        self.__num_hab = num_hab
        self.__reservada = reservada
        self.__cliente = cliente

    def __init__(self, num_hab, reservada):
        self.__num_hab = num_hab
        self.__reservada = reservada

    @property
    def num_hab(self):
        return self.__num_hab

    @num_hab.setter
    def num_hab(self, num_hab):
        self.__num_hab = num_hab

    @property
    def reservada(self):
        return self.__reservada

    @reservada.setter
    def reservada(self, reservada):
        self.__reservada = reservada

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    def __str__(self):
        if(self.reservada):
            return "HAB "+str(self.__num_hab)+" - RESERVADA -"+str(self.__cliente)
        else:
            return "HAB "+str(self.__num_hab)+" - LIBRE"


def menu_hotel():
    list_hab = list()
    hab = -1
    list_hab.append(Habitacion(1,False))
    list_hab.append(Habitacion(2,False))
    list_hab.append(Habitacion(3,False))
    list_hab.append(Habitacion(4,False))
    list_hab.append(Habitacion(5,False))

    while(hab != 0):
        for hab in list_hab:
            print(hab)
        hab = int(input("\nElige habitación (cero para salir): "))

        if(list_hab[hab-1].reservada == False):
            dni = input("Introduce DNI: ")
            nombre = input("Introduce nombre: ")
            apellidos = input("Introduce apellidos: ")
            list_hab[hab-1].cliente = Cliente(dni,nombre,apellidos)
            list_hab[hab-1].reservada = True
        else:
            print("Lo siento! La habitacion ya esta reservada\n")

menu_hotel()



