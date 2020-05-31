# -*- coding: utf-8 -*-
"""
Created on Wed May 13 19:32:19 2020
@author: Eliud Campa
"""
import pyaudio,wave,time
output_file = "led_encendido.wav"
audio = pyaudio.PyAudio()
while input("Por favor presiona e para ingresar y s para terminar ") != 's':
    stream = audio.open(format = pyaudio.paInt16,channels = 2,rate = 44100,input = True,frames_per_buffer = 1024)
    print("* recording")
    frames = []
    for i in range(0,int(44100/1024*4)):
        data = stream.read(1024)
        frames.append(data)
    print("* done recording")
    stream.stop_stream()
    stream.close()
    audio.terminate()
    output_file = input("Introduce el nombre del archivo ")
    wf = wave.open(output_file, 'wb')
    wf.setnchannels(2)
    wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    wf.setframerate(44100)
    wf.writeframes(b''.join(frames))
    wf.close()
    for x in range(0,3):
        print("Generando archivo...")
        time.sleep(0.7)
    print("Arvhvo generado éxitosamente")