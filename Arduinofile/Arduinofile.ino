#include <ESP8266WiFi.h>

#include <FirebaseArduino.h>
#define a  D0
#define b  D1
#define c  D2

#define HOST "https://sapj01.firebaseio.com/"
#define AUTH "Y5XDIp40C18wMvOKSf0iyT4BTWmtFtTUcSKV3M5k"
#define ssid "Insecure Channel"
#define pass "divyansh"

String path = "/" ;

void setup() {
  Serial.begin(115200);
  pinMode(A0,INPUT);
  pinMode(D0,OUTPUT);
  pinMode(D1,OUTPUT);
  pinMode(D2,OUTPUT);
  
  // connect to wifi.
  WiFi.begin(ssid, pass);
  Serial.print("connecting");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  Serial.println();
  Serial.print("connected: ");
  Serial.println(WiFi.localIP());
  
  Firebase.begin(HOST,AUTH);
}

void loop(){

    
//getInteger()
    int fan = Firebase.getInt("fan");
    int light = Firebase.getInt("light");
    int tv = Firebase.getInt("tv");
    int music = Firebase.getInt("music");
    delay(200);
    Serial.println(fan);
    Serial.println(light);
    Serial.println(tv);
    Serial.println(music);
    Serial.println("........................");
    
    if (Firebase.failed()) {
      Serial.println(Firebase.error());  
      return;
  }
  
}
