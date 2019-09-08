#include <ESP8266WiFi.h>

#include <FirebaseArduino.h>

#define HOST "https://sapj01.firebaseio.com/"
#define AUTH "Y5XDIp40C18wMvOKSf0iyT4BTWmtFtTUcSKV3M5k"
#define ssid "Insecure Channel"
#define pass "divyansh"

int t = 0;

void setup() {
  Serial.begin(115200);
  
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
t=t+1;
    

    int temp = Firebase.getInt("temp");
    Firebase.setFloat("abc",t);
    delay(1000);
//    int fan = Firebase.getFloat("fan");
//    int light = Firebase.getInt("light");
//    int tv = Firebase.getInt("tv");
//    int music = Firebase.getInt("music");
    
//    Serial.println(fan);
//    Serial.println(light);
//    Serial.println(tv);
//    Serial.println(music);
  Serial.println(temp);
  Serial.println(t);
  Serial.println("........................");
  
  
    if (Firebase.failed()) {
      Serial.println(Firebase.error());  
      return;
  }

  
  
}
