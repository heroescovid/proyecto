"""
Created on Sat May 16 01:51:12 2020
@author: Said Campa
"""
import pyaudio,wave   
#sound_output = wave.open(r"C:\Users\Marco\.spyder\led_encendido.wav","rb"):{
while input("Por favor presiona e para ingresar y s para salir ") != 's':
    dato = input("Dame el archivo a reproducir ")
    sound_output = wave.open(dato)
    sound = pyaudio.PyAudio()  
    stream = sound.open(format = sound.get_format_from_width(sound_output.getsampwidth()),channels = sound_output.getnchannels(),rate = sound_output.getframerate(),output = True)
    data = sound_output.readframes(1024)  
    while data:  
        stream.write(data)  
        data = sound_output.readframes(1024)    
    stream.stop_stream()  
    stream.close()  
    sound.terminate()  