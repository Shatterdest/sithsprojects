/*  Yi Xia
 *  P8GR13
*/
  
  #include <PRIZM.h>      // include the PRIZM library (Speak the language!)

  PRIZM p;            // instantiate a PRIZM object "prizm" so we can use its functions (Call Code!)

void setup() {

  p.PrizmBegin();   // initialize the PRIZM controller (Wake up!)

}

void loop() {

  p.setRedLED(HIGH);
  p.setGreenLED(LOW); // turn red led on and off w/ 1s delay
  delay(414);
  p.setRedLED(LOW);
  p.setGreenLED(HIGH);
  delay(414);

  // repeat this code in a loop

}
