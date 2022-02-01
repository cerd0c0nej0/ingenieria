# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 08:50:52 2022

@author: LENOVO
"""
"""
#crear lista
list = []
salir = False
while salir == True :
    
    print("----------MENU--------")
    print("1.- Lista de alumnos")
    print("2.- Resgistrar alumno")
    print("3.- Quitar alumno")
    print("4.- Salir")
    print("---------------------")

option = int(input("seleccione una opcion [1 - 2 - 3 - 4]:"))

if option == 1 :
    #muestro los alumnos 
    for alumno in list:
        print (alumno)
elif option ==2:
    new_alumno = input("ingrese nombre completo del alumno")
    list.appened(new_alumno)
elif option ==3:
    list.remove(list(0))    
elif option ==4 :
    print("bye")
    salir = True
else:
    print("porfavor ingrese una opcion valida [1, 2, 3]")
    
print(f'la opcion seleccionada es :{option}')    
print (list)
        """
       # crear una list
list = []

salir = False
while salir !=True:
    print("---------------Menu--------------------")
    print("1.- Listar Alumnos")
    print("2.- Registrar Alumno")
    print("3.- Eliminar ")
    print("4.- Salir")
    print("-----------------------------------")
    option = int(input("Seleccione una Opcion [1-2-3-4]:"))
    
    ## opcion 1 list alumno
    if option == 1:
        # muestro los alumnos
        print ("La list de alumno es:")
        for alumno in list:
            print (alumno)
    # opcion 2 agregar alumno
    elif option == 2:
        new_alumno = input("Ingrese Nombre Completo de Alumno:")
        list.append(new_alumno)
    elif option == 3:
        list.remove(alumno_quitar)

    elif option == 4:
        print ("bye!")
        salir = True
    else:
       print("Porfavor ingrese una opcion valida [1, 2 , 3, 4]")
        
        
print (f'la opcion seleccionada es : {option}')

    
