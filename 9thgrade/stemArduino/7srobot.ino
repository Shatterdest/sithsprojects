/*  Yi Xia
 *  P8GR13
*/
  
  #include <PRIZM.h>      // include the PRIZM library (Speak the language!)

  PRIZM p;            // instantiate a PRIZM object "prizm" so we can use its functions (Call Code!)

void setup() {

  p.PrizmBegin();   // initialize the PRIZM controller (Wake up!)
  p.setMotorInvert(1, 1);
  p.setMotorInvert(2,2);

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
  p.setMotorPowers(35,35);
  delay(125);
  p.setMotorPowers(52,52);
  delay(150);
  p.setMotorPowers(75, 75);
  delay(125);
  p.setMotorPowers(100,100);
  delay(6600);
  p.setMotorPowers(125,125);
  delay(500);
  p.setGreenLED(LOW);
  p.PrizmEnd();
  // repeat this code in a loop

}
