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
        
        #Sophia
        s = (r.recognize_google(audio))
        message = s.lower()
        print(message)
        if message == 'sofia':
            message = 'sophia'
        if ('sophia') in message:
            recog()
        if(message == 'goodbye' or message == 'good bye' or message == 'no'):
            sophia.say('Goodbye,Sir!')
            sophia.runAndWait()
            break
        if(message == 'thank you' or message == 'thankyou'):
            sophia.say('Anything else sir?')
            sophia.runAndWait()
        if(message == 'yes'):
            recog()
        
