/*  Yi Xia
 *  P8GR13
*/
  
  #include <PRIZM.h>      // include the PRIZM library (Speak the language!)

  PRIZM p;            // instantiate a PRIZM object "prizm" so we can use its functions (Call Code!)

void setup() {

  p.PrizmBegin();   // initialize the PRIZM controller (Wake up!)
  p.setMotorInvert(1, 1);
  //p.setMotorInvert(2,2);

}

void loop() { //lights for 60 time
  for(int counter = 0; counter<60; counter++) {
    lights();
  }

 for(int counter = 0; counter<4; counter++) { //forward and backward 4 time
  forward();
  backward();
  }
p.PrizmEnd();
}

void lights() { //light cadence
  p.setRedLED(HIGH);
  p.setGreenLED(HIGH);
  delay(50);
  p.setRedLED(LOW);
  p.setGreenLED(LOW);
  delay(50);
}

void forward() { //forward and break
 p.setMotorPowers(40,40);
 delay(500);
 p.setMotorPowers(125,125);
 delay(500);
 }

 void backward() { //backward and break
 p.setMotorPowers(-40,-40);
 delay(500);
 p.setMotorPowers(125,125);
 delay(500);
 }
