import os

os.system("cls")

opcion1 = int
banderanumeroCel = 0
banderaCorreo= int
usuario1=None
usuario2=None
usuario3=None
contrasena1=None
contrasena2=None
contrasena3=None

while opcion != 3:
    print("1) Inicio sesión")
    print("2) registrar usuario")
    print("3) salir")

    opcion = input("Seleccione una opcion 1); 2); 3)")

    if opcion ==1 and (usuario1 ==None or usuario2==None or usuario3 ==None): #Si opcion 1 y en los datos 3 datos de usuarios y contraseñas siguen en estado None se ejecuta lo siguiente
        print("Debe registrar un usuario antes de continuar")

            
    elif opcion == 1 and (usuario1 != None or usuario2!=None or usuario3 !=None):
        
                print("1) Realizar llamada")
                print("2) Enviar correo electronico")
                print("3) Cerrar sesión")
                
                opcion1=input("Ingrese una opcion 1); 2); 3)")
            
            
                if opcion1==1:
                    while banderanumeroCel == 1:
                        numeroCel=input("Ingrese el numero de celular")
                        for i in range(numeroCel):
                            if i ==8 and numeroCel.startswith("9"):
                                print("Favor Ingrese un numero con 9 digitos")
                                banderanumeroCel = 0
                            else:
                                print("Favor Ingrese un numero de 9 digitos")
                                banderanumeroCel = 1
                                
                if opcion1==2:
                    while banderaCorreo ==1:
                        correo=input("Ingrese un correo electronico\n")
                        for x in range(correo):
                            if x == "@":
        
        
    elif opcion ==2:
                    
                    usuario1=input("Ingrese un nombre de usuario")
                    contrasena1=input("Ingrese una contraseña")
                    print("A ingresado los datos correctamente")
                    
                    print("1) Inicio sesión")
                    print("2) registrar usuario")
                    print("3) salir")
                    
        