"""
    Created on Sat May 16 02:20:55 2020
    @author: Said Campa
"""
import serial,time
flag = 0
stm32_port = serial.Serial("COM10",19200)
print("Bienvenido al menú principal:")
print("Opcion 1 Ingrese s para salir del menú principal")
print("Opcion 2 Ingrese e para entrar al menu principal")
print("Opcion 3 Ingrese t para terminar la ejecución del programa principal")
flag = input("Esperando comando...... ")
while flag != 't':
    if flag == 'e':
        flag = input("Ingrese ID del dispositivo y el tiempo de intermitencia deseado ")
        while flag != 's' and flag != 't':
            dato = int(flag)
            for dato in range(0,dato):
                stm32_port.write('1')
                time.sleep(.290)
                stm32_port.write('0')
                time.sleep(.290)
            flag = input("Ingrese ID del dispositivo y el tiempo de intermitencia deseado ")
    if flag == 's':
        print("Menú principal cerrado para reingresar por favor ingrese alguna de las siguientes opciones")
        print("Opcion 1 Ingrese e para entrar al menu principal")
        print("Opcion 2 Ingrese t para terminar la ejecución del programa principal")
        flag = input("Esperando comando...... ")
print("Ejecución terminada del programa principal")        
for dato in range(0,3):
    print("Cerrnado comunicación serie......")
    time.sleep(0.7)
stm32_port.close()
print("Comunicacion serie cerrada")         