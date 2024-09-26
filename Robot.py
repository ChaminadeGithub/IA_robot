# importation des fonctionnalites des plugins installed
import speech_recognition as sr
import pyttsx3 as ttx
import pywhatkit
import datetime


listener = sr.Recognizer()
engine = ttx.init()
voice = engine.getProperty('voices') # on definit la voix du robot
engine.setProperty('voice', 'french')  

def parler(text):
    engine.say(text)
    engine.runAndWait()

def ecouter():
    try:
        with sr.Microphone() as source:
            print("Je vous écoute...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='fr-FR')
            # rec = rec.lower()
            # print(rec)
    except:
        pass
    return rec

def assistant_chaminade():
    rec = ecouter()
    print(rec)
    if 'bonjour' or 'bonsoir' or 'salut' or 'coucou' in rec:
        parler('Salut, ravi de vous entendre a nouveau, comment puis-je vous aider ?')
    elif 'heure' in rec:
        heure = datetime.datetime.now().strftime('%H:%M')
        parler('Il est ' + heure)
        print(heure)
    elif 'joue la musique' or 'la chanson' or 'une musique' in rec:
        parler('Je ne sais pas jouer de la musique, mais je peux vous chercher une musique de votre choix')
        check = rec.replace('joue musique', '')
        parler('Je recherche ' + check)
        print(check)
        pywhatkit.playonyt(check)    #permet de faire ou lancer la musique

    elif 'Recherche' in rec:
        check = rec.replace('recherche', '')
        parler('Je recherche ' + check)
        print(check)
        pywhatkit.search(check)
        # pywhatkit.playonyt(check)    #permet de faire ou lancer lA RECHERCHE
    # elif    'ouvre' in rec:
    #     check = rec.replace('ouvre', '')
    #     parler('Je recherche ' + check)
    #     print(check)
    #     webbrowser.open('https://www.google.com/search?q=' + check)
    elif 'ton nom' or 'tu t''appelles' or 'presente toi' or 'qui es-tu' :
        parler('Je suis un robot, une intelligence capable de parler, un assistant créé par Mr. Chaminade')
    elif 'merci' or 'd''accord' or 'ok' in rec:
        parler('ravi que vous ayez demander a me connaitre')
    # elif 'au revoir' in rec:
    #     parler('Au revoir')
    elif 'qu''est-ce que tu sais faire' in rec:
        parler('Je peux vous aider à rechercher des informations sur internet, vous dire l''heure, jouer de la musique, et vous dire votre nom')
    elif 'comment tu vas' in rec:
        parler('Je vais bien, merci')
    elif 'tu es un robot' in rec:
        parler('Oui, je suis un robot')
    elif 'tu es intelligent' in rec:
        parler('Oui, je suis intelligent')
    elif 'tu es un robot intelligent' in rec:
        parler('Oui, je suis un robot intelligent')
    elif 'tu es un robot intelligent qui peut faire des choses' in rec:
        parler('Oui, je suis un robot intelligent qui peut faire des choses')
    elif 'tu es un robot intelligent qui peut faire des choses comme' in rec:
        parler('Oui, je suis un robot intelligent qui peut faire des choses comme vous dire l''heure, jouer de la musique, et vous dire votre nom')
    elif 'Merci, Au revoir' in rec: 
        parler('Au revoir')
        exit()
    else:
        parler('Je ne comprends pas ce que vous dites')


while True:
    assistant_chaminade()










    # rec = ecouter()
    # if 'bonjour' in rec:
    #     parler('Bonjour, comment puis-je vous aider ?')
    # elif 'heure' in rec:
    #     heure = datetime.datetime.now().strftime('%H:%M')
    #     parler('Il est ' + heure)
    # elif 'joue' in rec:
    #     song = rec.replace('joue', '')
    #     parler('Je joue ' + song)
    #     pywhatkit.playonyt(song)
    # elif 'au revoir' in rec:
    #     parler('Au revoir')
    #     exit()
    # else:
    #     parler('Je ne comprends pas')