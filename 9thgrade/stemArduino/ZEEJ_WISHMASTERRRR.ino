/*  Yi Xia
 *  P8GR13
*/
  
  #include <PRIZM.h>      // include the PRIZM library (Speak the language!)

  PRIZM p;            // instantiate a PRIZM object "prizm" so we can use its functions (Call Code!)

void setup() {

  p.PrizmBegin();   // initialize the PRIZM controller (Wake up!)
  p.setMotorInvert(1, 2);
  //p.setMotorInvert(2,2);

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
  p.setMotorPower(1,10);
  delay(150);
  p.setMotorPower(1, 20);
  delay(150);
  p.setMotorPower(1,30);
  delay(400);
  p.setMotorPower(1,40);
  delay(400);
  p.setMotorPower(1,50);
  delay(400);
  p.setMotorPower(1,60);
  delay(450);
  p.setMotorPower(1, 70);
  delay(450);
  p.setMotorPower(1,80);
  delay(500);
  p.setMotorPower(1,90);
  delay(5
  0);
  p.setMotorPower(1,100);
      
  delay(7000);
  p.setGreenLED(LOW);
  p.PrizmEnd();
  // repeat this code in a loop

}
