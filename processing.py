#!/usr/bin/python
def recog():
    import speech_recognition as sr
    import pyaudio
    import wave
    import pyttsx3 

    from firebase import firebase

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 4
    WAVE_OUTPUT_FILENAME = "output.wav"

    firebase = firebase.FirebaseApplication('https://sapj01.firebaseio.com/')
    sophia = pyttsx3.init()
    
    sophia.say('Yes Rishi, What can I do for you?')
    sophia.runAndWait()
    
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    r = sr.Recognizer()
    output = sr.AudioFile('output.wav')
    with output as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.record(source)

    data = ['music','tv','fan','light']
    onoff = ['on','off']

    
    try:
        text = r.recognize_google(audio)
        print('Did you just say :', format(text))
        print(data[text.lower()])

    except:
        print('')

    
    text = r.recognize_google(audio)
    text = text.lower()
    temp = text.split()

    if text == 'reset':
        for i in data:
            result = firebase.put('/',i,0)


    
    for i in temp:
        for j in data:
            if i == j:
                for k in temp:
                    if k == onoff[1]:
                        result = firebase.put('/',j,0)
                        mod = 'Turning off the '+j
                        sophia.say(mod)
                        sophia.runAndWait()
                        print("Uploaded: ",result)
                        
                        
                    if k == onoff[0]:
                        result = firebase.put('/',j,1)
                        mod = 'Turning on the '+j
                        sophia.say(mod)
                        sophia.runAndWait()
                        print("Uploaded: ",result)
                        
                        
    
    
    sophia.say('Anything else, Sir?')
    sophia.runAndWait() 



