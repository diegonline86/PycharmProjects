# -*- coding: utf-8 -*-
agenda = dict()
opcion = -1

while(opcion!=0):
    print("\nAGENDA ELECTRÓNICA")
    opcion = int(input("1. Agregar contacto"
                       "\n2. Eliminar contacto"
                       "\n3. Mostrar un contacto"
                       "\n4. Mostrar todos los cotactos"
                       "\n5. Limpiar agenda"
                       "\n0. Salir"
                       "\n\nElige opcion: "))
    if(opcion == 1):
        nombre = input("Introduce nombre de contacto: ")
        tel = input("Introduce numero de teléfono: ")
        agenda[nombre] = tel
    elif(opcion == 2):
        nombre = input("Introduce nombre de contacto: ")
        agenda.pop(nombre)
    elif(opcion == 3):
        nombre = input("Introduce nombre de contacto: ")
        print(agenda.__getitem__(nombre))
    elif(opcion == 4):
        print("\nContactos\n",agenda)
    elif(opcion == 5):
        res = input("¿Realmente desea limpiar su agenda si(S), no(N)? ")
        if(res == 'S' or res == 's'):
            agenda.clear()