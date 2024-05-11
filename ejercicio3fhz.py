import os, time
os.system("cls")
#Ultimo comentario para comprobar si se subio a git

banderaMenu = True
banderaFono = True
user1=None
user2=None
user3=None
pass1=None
pass2=None
pass3=None

while banderaMenu:
    try:
        os.system("cls")
        print("Iniciar sesión")
        print("Registrar usuario")
        print("Salir")
        opcion  =int(input("Escoga una opcion\n"))
        if opcion ==1:
            if (user1 is None and pass1 is None) and (user2 is None and pass2 is None) and (user3 is None and pass3 is None):
                print("Es necesario registrar un usuario antes de poder continuar.")
                time.sleep(2)
                continue
            else:
                usuario= input("Ingrese un Usuario: \n")
                password = input("Ingrese una Contraseña: \n")
                if (usuario == user1 and password == pass1) or (usuario == user2 and password == pass2) or (usuario == user2 and password == pass2):
                    os.system("cls")
                    print("t\Menu Telefonica")
                    print("1) Realizar llamada")
                    print("2) Enviar Correo Electronico")
                    print("3) Cerrar sesión")
                    opcion1= int(input("Seleccione una opcion\n"))
                
                    if opcion1 ==1:
                        while banderaFono:
                            print("1. Realizar llamada")
                            fono = input("Ingresar numero de telefono\n")
                            if len(fono) == 9 and fono.startswith("9"):
                                print(f"Llamando al numero {fono}")
                                time.sleep(2)
                                banderaFono =False
                            else:
                                print("Favor ingresar un numero con 9 digitos y que comience con el numero 9.")
                    if opcion1 ==2:    
                        correo = input("Ingrese correo\n")
                        while "@" not in correo:
                            correo = input("Favor recordar que el correo debe contener el @ \n")
                        mensaje = input("Favor ingresar el mensaje a enviar\n")
                        print(f"De: {user1}")
                        print(f"Correo:  {correo}")
                        print(f"Mensaje:  {mensaje}")
                        time.sleep(2)
                        continue


        if opcion == 2:
            print("\tMenu REGISTRAR USUARIO")
            user1= input("Favor ingresar el usuario 1:\n")
            pass1= input("Favor ingresar contraseña 1:\n")
            opcion3=input("Quiere seguir registrando usuarios? 1)Si: 2)NO:\n")
            if opcion3 == 1:
                user2= input("Favor ingresar el usuario 2:\n")
                pass2= input("Favor ingresar contraseña 2:\n")
                opcion=input("Quiere seguir registrando usuarios? 1)Si: 2)NO:\n")
                if opcion3 == 1:
                    user3= input("Favor ingresar el usuario 3:\n")
                    pass3= input("Favor ingresar contraseña 3:\n")
                    print("USUARIOS CREADOS EXITOSAMENTE")
                    print(f"usuario 1: {user1}")
                    print(f"contraseña 1: ******")
                    print(f"usuario 2: {user2}")
                    print(f"contraseña 2: ******")
                    print(f"usuario 3: {user3}")
                    print(f"contraseña 3: ******")
                    time.sleep(1)
                    continue

                else:
                    print("USUARIOS CREADOS EXITOSAMENTE")
                    print(f"usuario 1: {user1}")
                    print(f"contraseña 1: ******")
                    print(f"usuario 2: {user2}")
                    print(f"contraseña 2: ******")
                    time.sleep(1)
                    continue
            else:
                print("USUARIOS CREADOS EXITOSAMENTE")
                print(f"usuario !: {user1}")
                print(f"contraseña 1: ******")
                time.sleep(1)
                continue

        if opcion == 3:
            print("OPCION 3")
            print("Saliendo del programa")
            break
    except:
        print("Ingrese una opcion valida")