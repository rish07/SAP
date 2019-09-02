#!/usr/bin/python
def recog():
    import speech_recognition as sr
    import pyaudio
    import wave

    from firebase import firebase

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "output.wav"

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

    data = {'reset':0,'turn on the fan':1,'turn off the fan':2,'turn on the light one':3,'turn off the light one':4,'turn on the light to':5,'turn off the light to':6}

    text = r.recognize_google(audio)
    try:
        text = r.recognize_google(audio)
        print('Did you just say :', format(text))
        print(data[text.lower()])
    except Exception:
        print('Sorry ! did not catch that. Shall we try again ? ')



    firebase = firebase.FirebaseApplication('https://sapj01.firebaseio.com/')

    result = firebase.put('/','command',data[text.lower()])
    print("Uploaded: ",result)


recog()