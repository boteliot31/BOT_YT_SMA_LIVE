
"""
                LIEN avec  VOCAL ASSISTANT.py
YT   : Hack Master
Vid  : Comment transcrire la voix avec python

https://www.youtube.com/watch?v=VyJgO_t0bX0
https://www.youtube.com/watch?v=VyJgO_t0bX0


"""
"""
pip install SpeechRecognition
pip install PyAudio
pip install pyttsx3
pip install pywhatkit
"""

import speech_recognition as sr
import pyttsx3  as ttx
# import pywhatkit
import datetime


r = sr.Recognizer()

with sr.Microphone() as source:
    print(" Speak NOW !!!!!  ")
    audio =r.listen(source)

    try:
        text = r.recognize_google(audio, language='fr-FR')
        print("Did You said this  :  {}  ??".format(text))

    except:
        print("Sorry repeat   !!!!!!  ")

