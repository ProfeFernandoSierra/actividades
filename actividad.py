import time,os
user1 = None
pass1 = None
user2 = None
pass2 = None
user3 = None
pass3 = None

while True:
    os.system("cls")
    print("1. Iniciar Sesion")
    print("2. Registro usuario")
    print("3. Salir")
    try:
        opcion = int(input("ingrese una opcion\n"))
        if opcion > 0 and opcion < 4:
            if opcion == 1:
                os.system("cls")
                print("1. Iniciar Sesion")
                if (user1 is None and pass1 is None) and (user2 is None and pass2 is None) and (user3 is None and pass3 is None):
                    print("no existen usuarios para ingresar, favor de registarse")
                    time.sleep(2)
                    continue
                else:
                    username = input("ingrese su usuario\n")
                    password = input("ingrese password\n")
                    if (username == user1 and password == pass1):
                        while True:
                            print("1. Realizar llamada")
                            print("2. Enviar correo electronico")
                            print("3. Salir")
                            try:
                                opcion2 = int(input("ingrese una opcion\n"))
                                if opcion2 > 0 and opcion2 < 4:
                                    if opcion2 == 1:
                                        print("Realizar llamada")
                                    elif opcion2 == 2:
                                        print("Enviar correo electronico")
                                    elif opcion2 == 3:
                                        print("Salir")
                                        break
                            except:
                                print("opcion ingresada no existe")
                    else:
                        print("usuario y/o contraseña son incorrectos")
                        time.sleep(2)
                        continue
            elif opcion == 2:
                os.system("cls")
                print("2. Registro usuario")
                user1 = input("ingrese usuario\n")
                pass1 = input("ingrese password\n")
                print("usuarios creados exitosamente")
                usuario = int(input("desea agregar otro usuario?  1.si  2.no\n"))
                if usuario == 1 :
                    user2 = input("ingrese usuario\n")
                    pass2 = input("ingrese password\n")
                    print("usuarios creados exitosamente")
                    usuario = int(input("desea agregar otro usuario?  1.si  2.no\n"))
                    if usuario == 1 :
                        user3 = input("ingrese usuario\n")
                        pass3 = input("ingrese password\n")
                        print("usuarios creados exitosamente")
                    
            elif opcion == 3:
                print("3. Salir")
                break
            else:
                print("opcion no existe")
    except:
        print("opcion ingresada no existe")