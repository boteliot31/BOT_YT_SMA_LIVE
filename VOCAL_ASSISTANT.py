"""
YT : FORMASYS
ASSISTANT VOCAL

"""
"""
LIEN avec SPEECH.py


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

listener = sr.Recognizer()
engine = ttx.init()
#engine = ttx.init()
voice = engine.getProperty('voices')
engine.setProperty('voice','french')

def parler(text):
    # engine = ttx.init(text)
    engine.say(text)
    engine.runAndWait()

def ecouter():
    try:
        with sr.Microphone() as source:
            print("Vous pouvez parlez maintenant, car j ecoute !!! (dit : >> BONJOUR <<)")
            parler("Vous pouvez parlez maintenant, car jécoute !!! (dit : >> BONJOUR <<)")            
            voix=listener.listen(source)
            command=listener.recognize_google(voix,language='fr-FR')
            command.lower()
    except:
        pass
    return command

def lancer_assistant():
    command=ecouter()
    print(command)
    if 'mets la chanson de' in command:
        chanteur=command.replace('mets la chanson de','')
        print(chanteur)
      #. pywhatkit.playonyt(chanteur)
    elif 'heure' in command:
        heure=datetime.datetime.now().strftime('%H:%M')
        parler('il est'+heure)
    elif ('Bonjour' or 'Hello') in command:
        parler(' Bonjour PAPY cest moi. Ton seul ami  !!!!!  ')
        parler(' Bonjour PAPY , Est ce que je dois rajouter une note OBSIDIAN, OUI ou NON  ? ')
        parler(' ou prefere tu , que , je modifie la note OBSIDIAN de JOUR , OUI ou NON  ? ')
        parler(' Bonjour PAPY , Je ne parle pas lingala  ! ')
        parler(' NA LOBAKA LIT GALA NANOU Té   !  ')
    else:
        parler('je ne comprends pas .')


while True:
    lancer_assistant()