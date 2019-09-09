import time

from firebase import firebase
firebase = firebase.FirebaseApplication('https://sapj01.firebaseio.com/')

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!. You can achieve this by using 'sudo' to run your script")
GPIO.setmode(GPIO.BOARD)


GPIO.setup(29, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(31, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(33, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(35, GPIO.OUT, initial=GPIO.LOW)



while True:
    

    fanState = firebase.get('/','fan')
    tvState = firebase.get('/','tv')
    musicState = firebase.get('/','music')
    lightState = firebase.get('/','light')

    GPIO.output(29, fanState)
    GPIO.output(31, tvState)
    GPIO.output(33, musicState)
    GPIO.output(35, lightState)
    

    print(fan," ",tv," ",music," ",light)

    time.sleep(1)
