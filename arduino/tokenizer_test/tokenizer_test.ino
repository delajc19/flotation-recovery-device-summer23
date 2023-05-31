#define MAXMSG 30

char array[] = "AAAA;A1:3;B1:5;ZZZZ";
char msg[MAXMSG];
char *strings[10];
char *ptr = NULL;



void setup()
{
    Serial.begin(9600);
//    //Serial.print(array);
    byte index = 0;
    ptr = strtok(array, ":;");  // takes a list of delimiters
    while(ptr != NULL)
    {
        strings[index] = ptr;
        index++;
        ptr = strtok(NULL, ":;");  // takes a list of delimiters
    }
//    //Serial.println(index);
// print the tokens
    for(int n = 0; n < index; n++)
   { 
    Serial.println(strings[n]);
   }
}

void loop()
{
    int i = 0;
    while(Serial.available() > 0 && i < MAXMSG-1){
      delay(2);
      char c = Serial.read();
      msg[i] = c;
      i++;
    }

    for(i=i;i<MAXMSG;i++){
      msg[i] = '\0';
    }

    if (i > 0){
      byte index = 0;
     ptr = strtok(msg, ",");  // takes a list of delimiters
     while(ptr != NULL)
      {
          strings[index] = ptr;
          index++;
          ptr = strtok(NULL, ",");  // takes a list of delimiters
      }
      for(int n = 0; n < index; n++)
        { 
          Serial.println(strings[n]);
        }
    }

}
