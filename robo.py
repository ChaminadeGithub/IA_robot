import speech_recognition as sr
import pyttsx3 as ttx
import pywhatkit
import datetime
import time

listener = sr.Recognizer()
engine = ttx.init()
voices = engine.getProperty('voices')

# Sélectionnez la voix française ici
for voice in voices:
    if "French" in voice.name:  # Utilisez la bonne voix française
        engine.setProperty('voice', voice.id)

def parler(text):
    engine.say(text)
    engine.runAndWait()

def ecouter():
    rec = ''  # Valeur par défaut si aucune voix n'est détectée
    try:
        with sr.Microphone() as source:
            print("Je vous écoute...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='fr-FR')
    except Exception as e:
        print(f"Erreur lors de l'écoute : {e}")
    return rec

def assistant_chaminade():
    rec = ecouter()
    if rec:
        print(f"Reconnu : {rec}")
        parler(f"Vous avez dit: {rec}")

        if any(x in rec for x in ['bonjour', 'bonsoir', 'salut', 'coucou']):
            parler('Salut, ravi de vous entendre a nouveau, comment puis-je vous aider ?')
        elif 'heure' in rec:
            heure = datetime.datetime.now().strftime('%H:%M')
            parler('Il est ' + heure)
            print(heure)
        elif any(x in rec for x in ['joue la musique', 'la chanson', 'une musique']):
            parler('Je ne sais pas jouer de la musique, mais je peux vous chercher une musique de votre choix')
            check = rec.replace('joue la musique', '')
            parler('Je recherche ' + check)
            pywhatkit.playonyt(check)    # permet de lancer la musique
        elif 'recherche' in rec:
            check = rec.replace('recherche', '')
            parler('Je recherche ' + check)
            pywhatkit.search(check)
        elif any(x in rec for x in ['ton nom', 'tu t\'appelles', 'présente toi', 'qui es-tu']):
            parler('Je suis un robot, une intelligence capable de parler, un assistant créé par Mr. Chaminade')
        elif any(x in rec for x in ['merci', 'd\'accord', 'ok']):
            parler('Ravi que vous ayez demandé à me connaitre')
        elif 'au revoir' in rec:
            parler('Au revoir, à bientôt !')
            exit()
        else:
            parler('Je ne comprends pas ce que vous dites')

while True:
    assistant_chaminade()
    time.sleep(1)  # Petite pause pour éviter une surcharge
