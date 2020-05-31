import time,serial
serial_lec = 0
while serial_lec != 't':
    com_port = serial.Serial("COM10",9600)
    print("Bienvenido al menu princial comunicacion serial iniciada")
    while serial_lec != 's' and serial_lec != 't':
        if serial_lec == '1':
            com_port.write('1')
            print("Led encendido")
        if serial_lec == '0':
            com_port.write('0')
            print("Led apagado")
        serial_lec = input()
    if serial_lec == 's':
        com_port.write('0')
        for x in range(0,3):
            print("Cerrando comunicacion serial.......")
            time.sleep(0.7)
            com_port.close()
        print("Comunicacion serial cerrada con exito")
        time.sleep(0.4)
        print("Esperando nuevas instrucciones")
        serial_lec = input()
com_port.write('0')
for x in range(0,3):
    print("Cerrando programa principal......")
    time.sleep(0.7)
com_port.close()
print("Programa principal cerrado con exito")