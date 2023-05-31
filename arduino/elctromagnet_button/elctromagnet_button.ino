
const int buttonPin = 2;     // the number of the pushbutton pin
const int emPin =  12;      // the number of the em pin

// variables will change:
int buttonState = 0;         // variable for reading the pushbutton status

void setup() {
  // initialize the em pin as an output:
  pinMode(emPin, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  // read the state of the pushbutton value:
  buttonState = digitalRead(buttonPin);

  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
  if (buttonState == HIGH) {
    // turn em on:
    digitalWrite(emPin, HIGH);
    Serial.println("ON");
  } else {
    // turn em off:
    digitalWrite(emPin, LOW);
    Serial.println("OFF");
  }
}
