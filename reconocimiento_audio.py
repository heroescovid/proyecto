"""
    Created on Sat May 16 04:36:41 2020
    @author: Said Campa
"""
import wave,pyaudio,speech_recognition as sr
recogniser = sr.Recognizer()
sound_file = "comando_1.wav"
sound_outp = wave.open(r"C:\Users\Marco\.spyder\led_encendido.wav","rb")
sound = pyaudio.PyAudio()
with sr.AudioFile('led_encendido.wav') as source:
    audio = recogniser.listen(source)
    try:
        print("Reading audio file. Please, wait a moment...")
        text = recogniser.recognize_google(audio,language = 'es-ES')
        print(text)
    except:
        print("I am sorry! I can not understand!")