import time
import pyrebase

config = {
  "apiKey": "AIzaSyBhX0sgV4eKjZfK71KfuSWi3yi2iXJw47I",
  "authDomain": "sapj01.firebaseapp.com",
  "databaseURL": "https://sapj01.firebaseio.com",
  "storageBucket": "gs://sapj01.appspot.com/"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(29, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(31, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(33, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(35, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(37, GPIO.OUT, initial=GPIO.LOW)

except RuntimeError:
    print("Error importing RPi.GPIO!. You can achieve this by using 'sudo' to run your script")


while True:
    microState = db.child("microwave").get().val()
    tvState = db.child("tv").get().val()
    musicState = db.child("music").get().val()
    lightState = db.child("light").get().val()
    temp1 = db.child("temp1").get().val()

    GPIO.output(29, microState)
    GPIO.output(31, tvState)
    GPIO.output(33, musicState)
    GPIO.output(35, lightState)
    GPIO.output(37, temp1)
    
    #print(microState," ",tvState," ",musicState," ",lightState," ",temp1)

GPIO.cleanup(29,31,33,35,37)
