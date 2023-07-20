//#include <AltSoftSerial.h>

//#define rxPin 9
//#define txPin 8
#define magPin 12
#define MAXMSG 30

const int baud = 115200;

bool magOn = false;

//AltSoftSerial m64;

char msg[MAXMSG];
char *strings[10];
char *ptr = NULL;

int sec = 1;
void setup(){

    //define pin mode for electromagnet
  pinMode(magPin, OUTPUT);
  pinMode(1,OUTPUT);
  pinMode(0,INPUT);
  
  //define pin modes for TX and RX
  //irrelevant commands for altsoftserial
//  pinMode(rxPin, INPUT);
//  pinMode(txPin, OUTPUT);

  //begin serial
//  m64.begin(baud);
  Serial.begin(baud);
  
  Serial.write("wcv");
  delay(10);
  Serial.write("wcs,b,4");
  delay(10);
  Serial.write("wcc");
  delay(10);
  Serial.write("wcq,8,HelloTop");
  delay(100);

}

void loop(){
  int i = 0;
  while(Serial.available() > 0 && i < MAXMSG-1){
    delay(100);
    char c = Serial.read();
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
//      Serial.println(strings[n]);
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
//      Serial.println("MAGNET ON");
//    }
//    else{
//      digitalWrite(magPin, LOW);
//      Serial.println("MAGNET OFF");
//    }

    if(strncmp(strings[2],"fire",4)==0){
//      Serial.println("MAGNET FIRED");
      sec = atoi(strings[3]);
//      Serial.println(sec);
//      Serial.println(strings[3]);
      if(sec < 1){
        sec = 1;
      }
      if(sec > 30){
        sec = 30;
      }
      digitalWrite(magPin, HIGH);
      delay(sec*1000);
      digitalWrite(magPin, LOW);
      Serial.write("wcq,8,fired   ");
    }
    
  }
  i = 0;
}
