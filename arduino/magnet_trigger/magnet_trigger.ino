#include <SoftwareSerial.h>

#define rxPin 5
#define txPin 6
#define magPin 12

const int baud = 9600;

bool magOn = false;

//Set up a new SoftwareSerial object
SoftwareSerial mySerial = SoftwareSerial(rxPin, txPin);

String msg;


void setup() {
  //define pin mode for electromagnet
  pinMode(magPin, OUTPUT);
  
  //define pin modes for TX and RX
  pinMode(rxPin, INPUT);
  pinMode(txPin, OUTPUT);

  //begin serial
  mySerial.begin(baud);
//  Serial.begin(baud);

  //print begin of test
  mySerial.println("SoftwareSerial test 0001");
//  Serial.println("serial test 0001"); 
}

void loop() {
  //read message from COM3
  while (mySerial.available()) {
    delay(4);  //delay to allow byte to arrive in input buffer
    char c = mySerial.read();
    msg += c;
  }

  //if message from COM3 is not empty
  if(msg.length() > 0){
    //Indicate message coming from COM3
    mySerial.print("COM 3: ");
    
    //Print message to both serial monitors
    mySerial.println(msg);

    if(msg.substring(0,2).equalsIgnoreCase("on")){
      magOn = true; 
    }

    if(msg.substring(0,3).equalsIgnoreCase("off")){
      magOn = false;
    }
    
    if(msg.substring(0,4).equalsIgnoreCase("fire")){
      mySerial.println("MAGNET FIRED");
      digitalWrite(magPin, HIGH);
      delay(2000);
      digitalWrite(magPin,LOW);
    }

    if(magOn){
      digitalWrite(magPin, HIGH);
      mySerial.println("MAGNET ON");
    }
    else{
      digitalWrite(magPin, LOW);
      mySerial.println("MAGNET OFF");
    }

    //reset message variable
    msg = "";

  }

}
