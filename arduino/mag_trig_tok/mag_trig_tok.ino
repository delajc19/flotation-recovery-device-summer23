#include <SoftwareSerial.h>

#define rxPin 5
#define txPin 6
#define magPin 12
#define MAXMSG 30

const int baud = 9600;

bool magOn = false;

SoftwareSerial m64 = SoftwareSerial(rxPin, txPin);

char msg[MAXMSG];
char *strings[10];
char *ptr = NULL;

void setup(){

    //define pin mode for electromagnet
  pinMode(magPin, OUTPUT);
  
  //define pin modes for TX and RX
  pinMode(rxPin, INPUT);
  pinMode(txPin, OUTPUT);

  //begin serial
  m64.begin(baud);
//  Serial.begin(baud);

  m64.println("Hello there!");

}

void loop(){
  int i = 0;
  while(m64.available() > 0 && i < MAXMSG-1){
    delay(2);
    char c = m64.read();
    msg[i] = c;
    i++;
  }

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
    for(int n = 0; n < index; n++){
      m64.println(strings[n]);
    }
    
    if(strncmp(strings[2],"on",2)==0){
      magOn = true;
    }

    if(strncmp(strings[2],"off",3)==0){
      magOn = false;
    }

    if(magOn){
      digitalWrite(magPin, HIGH);
      m64.println("MAGNET ON");
    }
    else{
      digitalWrite(magPin, LOW);
      m64.println("MAGNET OFF");
    }

    if(strncmp(strings[2],"fire",4)==0){
      m64.println("MAGNET FIRED");
      digitalWrite(magPin, HIGH);
      delay(2000);
      digitalWrite(magPin, LOW);
    }
    
  }
  i = 0;
}
