#include <SoftwareSerial.h>

#define rxPin 5
#define txPin 6
#define magPin 12

const int baud = 9600;

bool magOn = false;

//Set up a new SoftwareSerial object
SoftwareSerial mySerial = SoftwareSerial(rxPin, txPin);

String stringCOM3;
String stringCOM14;


void setup() {
  //define pin mode for electromagnet
  pinMode(magPin, OUTPUT);
  
  //define pin modes for TX and RX
  pinMode(rxPin, INPUT);
  pinMode(txPin, OUTPUT);

  //begin serial and mySerial
  mySerial.begin(baud);
  Serial.begin(baud);

  //print begin of test
  mySerial.println("SoftwareSerial test 0001");
  Serial.println("serial test 0001"); // so I can keep track of what is loaded
}

void loop() {
  //read message from COM3
  while (mySerial.available()) {
    delay(4);  //delay to allow byte to arrive in input buffer
    char c = mySerial.read();
    stringCOM3 += c;
  }

  //read message from COM14
  while (Serial.available()) {
    delay(4);  //delay to allow byte to arrive in input buffer
    char b = Serial.read();
    stringCOM14 += b;
  }

  //if message from COM3 is not empty
  if(stringCOM3.length() > 0){
    //Indicate message coming from COM3
    Serial.print("COM 3: ");
    mySerial.print("COM 3: ");
    
    //Print message to both serial monitors
    Serial.println(stringCOM3.substring(0,1));
    mySerial.println(stringCOM3);

    if(stringCOM3.substring(0,2).equalsIgnoreCase("on")){
      magOn = true; 
    }

    if(stringCOM3.substring(0,3).equalsIgnoreCase("off")){
      magOn = false;
    }
    
    if(stringCOM3.substring(0,4).equalsIgnoreCase("fire")){
      digitalWrite(magPin, HIGH);
      delay(2000);
      digitalWrite(magPin,LOW);
      Serial.println("MAGNET FIRED");
    }

    if(magOn){
      digitalWrite(magPin, HIGH);
      Serial.println("MAGNET ON");
    }
    else{
      digitalWrite(magPin, LOW);
      Serial.println("MAGNET OFF");
    }

    //reset COM 3 message variable
    stringCOM3 = "";

  }

  //if message from COM14 is not empty
  if(stringCOM14.length() > 0){
    //Indicate message coming from COM14
    Serial.print("COM 14: ");
    mySerial.print("COM 14: ");
    
    //Print message to both serial monitors
    Serial.println(stringCOM14);
    mySerial.println(stringCOM14);

    //reset COM 14 message variable
    stringCOM14 = "";

  }

}
