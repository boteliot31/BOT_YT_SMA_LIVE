"""
LIEN avec SPEECH.py
YT :  Charlie Code
Vid : Creer un assistant vocal a laide de Python .  Vocal Assistant by Charlie Code
https://www.youtube.com/watch?v=3YzTTj7qM9k&t=667s
https://www.youtube.com/watch?v=3YzTTj7qM9k&t=667s
https://www.youtube.com/watch?v=3YzTTj7qM9k&t=667s
"""
"""
pip install SpeechRecognition
pip install PyAudio
pip install pyttsx3
pip install pywhatkit
"""
from fcntl import LOCK_WRITE
from urlib.request import urlopen     # acceder aux url ...
from googletrans import Translator    # pour la traduction ...
from random import choice

import speech_recognition as sr
import pyttsx3  as ttx     # pour convertir txt en audio   ...
# import pywhatkit
import datetime
import subprocess       # pour ouvir les applications
import wolframalpha      # api pour faire les calcule  ...
import webbrowser       # pour ouvrir les lien internet  ...
import wikipedia

listener = sr.Recognizer()
engine = ttx.init()
#engine = ttx.init()
voice = engine.getProperty('voices')
engine.setProperty('voice','french')

def assistant_voix(sortie):
    if sortie != None:
        voix = pyttsx3.init()
        print(" A.I. " + sortie)
        voix.say(sortie)
        voix.runAndWait()

def internet():
    try:
        urlopen("https://www.google.com", timeout = 1)
        return True
    except:
        return False  

def reconnaissance():
    r = sr.Recognizer()
    pas_compris = "Desole je nai pas compris  . "
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 0.7
        print(". . . . . . ")
        audio = r.listen(source) 
        if internet():
            try:
                vocal = r.recognize_google(audio, language = "fr-FR")  
                print(vocal)
                return vocal
            except:
                assistant_voix(pas_compris) 
        else:
            try:
                vocal = r.recognize_sphinx(audio, language = "fr-fr")  
                print(vocal)
                return vocal
            except:
                assistant_voix(pas_compris)             

def application(entree):
    if entree != None:
        dico_apps = {
            "note" : ["notepad", "note pad"],
            "sublime" : ["sublime text", "sublime texte"],
            "obs" : ["obs", "obs capture", "capture l ecran"],
            "edge" : ["microsoft edge", "edge"]
        }
        fini = False
        while not fini:
            for x in dico_apps["note"]:
                if x in entree.lower():
                    assistant_voix("Ouverture de Notepad  .. ")
                    subprocess.Popen("C:\\Windows\\System32\\notepad.exe")
                    fini = True
            for x in dico_apps["sublime"]:
                if x in entree.lower():
                    assistant_voix("Ouverture de Sublime  .. ")
                    subprocess.Popen("C:\\Windows\\System32\\notepad.exe")
                    fini = True
            for x in dico_apps["obs"]:
                if x in entree.lower():
                    assistant_voix("Ouverture de obs  .. ")
                    subprocess.Popen("C:\\Windows\\System32\\notepad.exe")
                    fini = True
            for x in dico_apps["edge"]:
                if x in entree.lower():
                    assistant_voix("Ouverture de edge  .. ")
                    subprocess.Popen("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
                    fini = True    

def calcul(entree):
    if entree != None:
        traducteur = Translator()
        traduction = traducteur.translate(text = entree, dest = "en").text
        app_id = "PLACEZ VOTRE IDE ICI / YOUR ID TAKE PLACE HERE ! ! ! "
        client = wolframalpha.Client(app_id)
        res = client.query(traduction)
        try:
            reponse = next(res.results).text
            traduction_reponse = traducteur.translate(text = reponse, dest = "fr").text  # initialisation du traducteur pcq wolfram fonctionne seulement en anglai
            assistant_voix("Le resultat est %d . " %(traduction_reponse))
        except:
            assistant_voix("Il y a une erreur, desole ...")

def sur_le_net(entree):
    if entree != None:
        if "youtube" in entree.lower():    # si youtube est prononce ...
            indx = entree.lower().split().index("youtube") # on suvegarde l index du mot dans indx  ...
            recherche = entree.lower().split()[indx +1:]  # on recupere ce quil est prononce a partir de indx+1 dans variable recherche ...
            if len(recherche) != 0:
                assistant_voix("recherche sur YouTube  .")
                webbrowser.open("http://youtube.com/results?search_query"+"+".join(recherche), new = 2) # on joint tous les element contenu dans recherche dans une seul chaine
            elif "wikipedia" in entree.lower():
                wikipedia.set_lang("fr")
                try:
                    indx = entree.lower().split().index("wikipedia")
                    recherche = entree.lower().replace("cherche sur wikipedia", "")
                    if len(recherche) != 0:
                        resultat = wikipedia.summary(recherche, sentence = 1) # resultat de la recherche de wikipedia ...
                        # on recupere le summary de la page, le nombre de ligne, dependant de la valeur de sentence ici = 1 ...
                        assistant_voix("recherche sur wikipedia .")
                        assistant_voix(resultat)
                except:
                        assistant_voix("Desole aucune page trouve sur Wiki ...")

            else:
                if "google" in entree.lower():      
                    indx = entree.lower().split().index("google")
                    recherche = entree.lower().split()[indx +1:]  
                    if len(recherche) != 0:
                        assistant_voix("recherche sur google  .")
                        webbrowser.open("http://google.com/search?q="+"+".join(recherche), new = 2)
                elif "cherche" in entree.lower():      
                    indx = entree.lower().split().index("cherche")
                    recherche = entree.lower().split()[indx +1:]  
                    if len(recherche) != 0:
                        assistant_voix("recherche sur google  .")
                        webbrowser.open("http://google.com/search?q="+"+".join(recherche), new = 2) 
                elif "recherche" in entree.lower():      
                    indx = entree.lower().split().index("recherche")
                    recherche = entree.lower().split()[indx +1:]  
                    if len(recherche) != 0:
                        assistant_voix("recherche sur google  .")
                        webbrowser.open("http://google.com/search?q="+"+".join(recherche), new = 2)  


def main():
    assistant_voix("Bonjour  . Quesce ce que je peux faire pour toi sur Google ou Youtube ou Wikipedia ??")
    fermer = ["arrete toi", "stop", "exit"]
    ouvrir = ["ouvre","lance", "peux tu ouvrir"] # pour ouvrir une application ...
    cherche = ["cherche sur youtube", "cherche sur google", "cherche sur wikipedia", "cherche"]  # pour chercher sur le web  ...
    calcul = ["calcul"]  

    actif = True
    while actif:
        if (entree := reconnaissance()) is not None:
            for x in range(len(fermer)):
                if fermer[x] in entree.lower():
                    assistant_voix("Au revoir   !!!! ")
                    actif = False
            for x in range(len(ouvrir)):
                if ouvrir[x] in entree.lower():
                    application(entree)
                    break
            for x in range(len(cherche)):
                if cherche[x] in entree.lower():
                    sur_le_net(entree)
                    break
            for x in range(len(calcul)):
                if calcul[x] in entree.lower():
                    calcul(entree)
                    break


if __name__ == '__main__':
    main()                




 
                                                                    
                    









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