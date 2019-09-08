from processing import recog
import speech_recognition as sr
import pyttsx3 
sophia = pyttsx3.init()
voices = sophia.getProperty('voices')
sophia.setProperty('voice', voices[1].id)
while(True):
    print('listening')
    r = sr.Recognizer()
    with sr.Microphone() as source:
        
        audio = r.listen(source)
        
        #JARVIS
        s = (r.recognize_google(audio))
        message = s.lower()
        print(message)
        if (message == 'hey sophia' or message == 'hi sophia' or message == 'hey sofia' or message == 'hi sofia'):
            recog()
        if(message == 'goodbye' or message == 'good bye'):
            sophia.say('Goodbye,Sir!')
            sophia.runAndWait()
            break
