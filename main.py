from processing import recog
import speech_recognition as sr
import pyttsx3 
jarvis = pyttsx3.init()
while(True):
    print('listening')
    r = sr.Recognizer()
    with sr.Microphone() as source:
        
        audio = r.listen(source)
        

        s = (r.recognize_google(audio))
        message = s.lower()
        print(message)
        if (message == 'hey jarvis' or message == 'hi jarvis'):
            recog()
        if(message == 'goodbye' or message == 'good bye'):
            jarvis.say('Goodbye,Sir!')
            jarvis.runAndWait()
            break
