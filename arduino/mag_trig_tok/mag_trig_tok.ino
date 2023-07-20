#include <AltSoftSerial.h>

//#define rxPin 9
//#define txPin 8
#define magPin 12
#define MAXMSG 30

const int baud = 9600;

bool magOn = false;

AltSoftSerial m64;

char msg[MAXMSG];
char *strings[10];
char *ptr = NULL;

int sec = 1;

void setup(){

    //define pin mode for electromagnet
  pinMode(magPin, OUTPUT);
  
  //define pin modes for TX and RX
  //irrelevant commands for altsoftserial
//  pinMode(rxPin, INPUT);
//  pinMode(txPin, OUTPUT);

  //begin serial
  m64.begin(baud);
  Serial.begin(baud);

  m64.println("Hello there!");

}

void loop(){
  int i = 0;
  while(m64.available() > 0 && i < MAXMSG-1){
    delay(8);
    char c = m64.read();
    msg[i] = c;
    i++;
  }

  //Pad the rest of the message with null characters
  for(i=i;i<MAXMSG;i++){
    msg[i] = '\0';
  }

  if(strlen(msg) > 0){
    byte index = 0;
    ptr = strtok(msg, ","); //takes a list of delimiters
    while(ptr != NULL){
      strings[index] = ptr;
      index++;
      ptr = strtok(NULL, ",");
    }

    //serial output for debugging recieved messages
//    for(int n = 0; n < index; n++){
//      m64.println(strings[n]);
//    }
//    
//    if(strncmp(strings[2],"on",2)==0){
//      magOn = true;
//    }
//
//    if(strncmp(strings[2],"off",3)==0){
//      magOn = false;
//    }
//
//    if(magOn){
//      digitalWrite(magPin, HIGH);
//      m64.println("MAGNET ON");
//    }
//    else{
//      digitalWrite(magPin, LOW);
//      m64.println("MAGNET OFF");
//    }

    if(strncmp(strings[2],"fire",4)==0){
//      m64.println("MAGNET FIRED");
      sec = atoi(strings[3]);
      Serial.println(sec);
      Serial.println(strings[3]);
      if(sec < 1){
        sec = 1;
      }
      if(sec > 30){
        sec = 30;
      }
      digitalWrite(magPin, HIGH);
      delay(sec*1000);
      digitalWrite(magPin, LOW);
      m64.write("wcq,5,fired");
    }
    
  }
  i = 0;
}
