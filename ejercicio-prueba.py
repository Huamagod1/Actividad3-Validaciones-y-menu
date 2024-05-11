import time, os
os.system("cls")
#crear un menu
#Opcion 1 debo crear el formulario de registro
#validar todos los campos
#opcion 2 debo crera un resumen del alumno inscrito, solo el admin puede acceder a esta vista
#solo puedo ver el resumen si soy admin y ademas existe el alumno
#debo crear una condicion y evaluar el nem para mandar una info "importante"
#opcion 3 solo debo romper el ciclo del menu


usuario="admin"
password="admin"


while True:
    os.system("cls")
    print("SISTEMA DE GESTION DE ALUMNOS")
    print("1) Registrar Alumno")
    print("2) Consultar Datos de Alumno")
    print("3) Salir\n")
    try:
        
            opcion=int(input("Seleccione una opcion\n"))
            
            if opcion ==1:
                
                print("REGISTRO DE ALUMNOS")
                
                nombre=input("Ingrese el nombre de alumno\n")
                while nombre == "":
                            nombre = input("El campo no puede venir vacio, ingrese nombre\n")
                            print(nombre)
                            time.sleep(2)
                
                
                direccion=input("Ingrese la dirección del alumno\n")
                while direccion == "":
                            direccion = input("El campo no puede venir vacio, ingrese nombre\n")
                            print(direccion)
                            time.sleep(2)
                            
                rut=int(input("Ingrese el rut del alumno\n"))
                while rut <= 500000 or rut >=39999999:
                    rut=int(input("Porfavor ingresar un rut mayor a 5000000 y menor a 39999999\n"))
                    time.sleep(2)
                
                edad=int(input("Ingrese la edad del alumno\n"))
                while edad <17 or edad > 90:
                   edad=int(input("Ingrese la edad del alumno\n"))
                correo= input("Ingrese el correo\n")
                while "@" not in correo:
                    correo=input("ingrese un correo con @, porfavor\n")
                
                nem= float(input("ingrese Nem\n")) 
                            
                            
            elif opcion ==2:
                print("CONSULTAR DATOS DEL ALUMNO")
                user=input("Ingrese el usuario")
                pas=input("Ingrese la contraseña")
                
                if usuario==user and password== pas:
                    rut_alumno = int(input("Ingrese el rut del alumno a consultar"))
                    print(f"rur: {rut_alumno}")
                    print(f"Nombre de alumno: {nombre}")
                    print(f"Edad: {edad}")
                    print(f"Direccion: {direccion}")
                    print(f"Correo: {correo}")
                
            elif opcion ==3:
                print("SALIENDO DEL PROGRAMA")
                break
    except:
        print("Opcion no existe ")
                    
                    