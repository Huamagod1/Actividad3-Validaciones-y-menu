import time,os

os.system("cls")
opcion=0
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

    opcion = int(input("Seleccione una opcion 1); 2); 3)\n"))

    if opcion ==1:
        print("INICIO DE SESIÓN")
        if (usuario1 ==None or usuario2==None or usuario3 ==None): #Si opcion 1 y en los datos 3 datos de usuarios y contraseñas siguen en estado None se ejecuta lo siguiente
            os.system("cls")
            print("No existen usuarios para acceder")
            print("Debe registrar un usuario antes de continuar")
            time.sleep(2)
            continue
        else:
              username = input("Ingrese un nombre de usuario\n")
              password = input("Ingrese su contrasela\n")
              if(username == usuario1 and password==contrasena1) or (username==usuario2 and password== contrasena2) or (username==usuario3 and password== contrasena3)
            
        
                print("1) Realizar llamada\n")
                print("2) Enviar correo electronico\n")
                print("3) Cerrar sesión\n")
                
                opcion1=input("Ingrese una opcion 1); 2); 3)\n")
            
                if opcion1==1:
                    while banderanumeroCel == 1:
                        numeroCel=input("Ingrese el numero de celular (debe comenzar con 9 y tener 9 digitos): \n")
                        for i in range(numeroCel):
                            if i ==8 and numeroCel.startswith("9"):
                                print("Favor Ingrese un numero con 9 digitos\n")
                                banderanumeroCel = 0
                            else:
                                print("Favor Ingrese un numero de 9 digitos\n")
                                banderanumeroCel = 1
                                
                if opcion1==2:
                    while banderaCorreo ==1:
                        correo=input("Ingrese su correo electronico\n")
                        for x in range(correo):
                            if x == "@":
                                 print("El correo se guardo exitosamente: ", correo)
                                 banderaCorreo = 0
                                 time.sleep(2)
                                 os.system("cls")
                                 mensaje =input("Ingresar el mensaje a enviar\n")
                                 print(f"DE: {username}")
                                 print(f"PARA: {correo}")
                                 print(f"DE: {username}")
                            elif opcion1 == 3:
                                  print("3.SALIENDO DE LA OPCION")
                            else:
                                print("Favor ingresar un correo con @") 
                                banderaCorreo = 1

                                 
        
        
    elif opcion ==2:
                    print("REGISTRO DE USUARIOS")
                    
                    usuario1=input("Ingrese un nombre de usuario: \n")
                    contrasena1=input("Ingrese una contraseña: \n")
                    opcion2 = input("¿Quiere seguir creando usuarios? 1) Si; 2)No\n")
                    if opcion2 == 1:
                          
                            usuario2=input("Ingrese un nombre de usuario: \n")
                            contrasena2=input("Ingrese una contraseña: \n")
                            opcion2 = input("¿Quiere seguir creando usuarios? 1)Si; 2)No\n")
                            if opcion2 == 1:
                            
                                usuario3=input("Ingrese un nombre de usuario: \n")
                                contrasena3=input("Ingrese una contraseña: \n")
                                print("La cantidad maxima de usuarios registrados se ha alcanzado exitosamente")
                                print(f"Usuario 1: {usuario1}\n")
                                print(f"Contraseña 1: {contrasena1}\n")
                                print(f"Usuario 2: {usuario2}\n")
                                print(f"Contraseña 2: {contrasena2}\n")
                                print(f"Usuario 3: {usuario3}\n")
                                print(f"Contraseña 3: {contrasena3}\n")
                            else:
                                    print("Usuarios creados correctamente")
                                    print(f"Contraseña 1: {contrasena1}\n")
                                    print(f"Usuario 2: {usuario2}\n")
                                    print(f"Contraseña 2: {contrasena2}\n")
                                    time.sleep(1)
                                    continue
                    else:
                          print("Usuarios creados correctamente")
                          print(f"Usuario 1: {usuario1}\n")
                          print(f"Contraseña 2: {contrasena1}\n")
                          time.sleep(1)
                          continue
    elif opcion == 3:
          print("OPCION 3")
          print("SALIENDO DEL PROGRAMA")
    else:
          print("Opcion no existe\n")
    
                    
                


                          

                    
