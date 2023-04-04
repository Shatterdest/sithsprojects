/*  Yi Xia
 *  P8GR13
*/
  
  #include <PRIZM.h>      // include the PRIZM library (Speak the language!)

  PRIZM p;            // instantiate a PRIZM object "prizm" so we can use its functions (Call Code!)

void setup() {

  p.PrizmBegin();   // initialize the PRIZM controller (Wake up!)
  p.setMotorInvert(1, 1);

}

void loop() {
  for(int counter = 1; counter<=2; counter++) {
  p.setRedLED(HIGH);
  p.setGreenLED(HIGH);
  delay(500);
  p.setRedLED(LOW);
  p.setGreenLED(LOW);
  delay(500);
  }
  p.setGreenLED(HIGH);
  delay(500);
  p.setMotorPowers(40, 40);
  delay(10000);
  p.setMotorPowers(0,0);
  p.setGreenLED(LOW);
  p.PrizmEnd();
  // repeat this code in a loop

}
