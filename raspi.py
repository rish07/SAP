import time
from firebase import firebase
firebase = firebase.FirebaseApplication('https://sapj01.firebaseio.com/')

while True:
    

    fan = firebase.get('/','fan')
    tv = firebase.get('/','tv')
    music = firebase.get('/','music')
    light = firebase.get('/','light')

    print(fan," ",tv," ",music," ",light)

    time.sleep(1)
