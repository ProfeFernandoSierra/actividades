import time,os
import datetime
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
                                if opcion2 == 1:
                                    os.system("cls")
                                    print("Realizar llamada")
                                    numero = input("Por favor, ingresa el número de celular (debe comenzar con 9 y tener 9 dígitos): \n")
                                    if len(numero) == 9 and numero.startswith('9'):
                                        print(f"Llamando al número {numero}... " )
                                        time.sleep(2)
                                        print("presione tecla para cortar")
                                        tecla = input()
                                        print("llamada finalizada")
                                    else:
                                        print("El número ingresado no es válido. Debe comenzar con 9 y tener 9 dígitos.\n")

                                elif opcion2 == 2:
                                    os.system("cls")
                                    print("Enviar correo electronico")
                                    correo = input("ingrese correo\n")
                                    while '@' not in correo:
                                        correo = input("ingrese correo, recuerde formato con @\n")
                                    mensaje = input("ingrese mensaje a enviar\n")
                                    print(f"DE: {username}")
                                    print(f"PARA: {correo}")
                                    print(f"MENSAJE: \n {mensaje}")
                                    time.sleep(4)
                                    print("presione tecla para volver al menu")
                                    tecla = input()
                                elif opcion2 == 3:
                                    os.system("cls")
                                    print("Cerrando sesion...")
                                    time.sleep(2)
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
                os.system("cls")
                print("3. Salir")
                break
            else:
                print("opcion no existe")
    except:
        print("opcion ingresada no existe")