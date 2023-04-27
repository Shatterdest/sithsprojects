/*  Yi Xia
 *  P8GR13
 */

#include <PRIZM.h>      // include the PRIZM library (Speak the language!)

PRIZM p; // instantiate a PRIZM object "prizm" so we can use its functions (Call Code!)

void setup() {

  p.PrizmBegin(); // initialize the PRIZM controller (Wake up!)
  p.setMotorInvert(1, 1);
  //p.setMotorInvert(2,2);
  Serial.begin(9600);

}

void loop() {
  for (int times = 0; times < 3; times++) {
    forwardThree();
    turn180();
    forwardThree();
  }
  p.PrizmEnd();
}

void forwardThree() { //forward exactly 3 ft
p.setMotorTargets(500,3950,500,3950);
delay(3000);
p.resetEncoders();
}

//void brake() {
//  p.setMotorPowers(125, 125);
//  delay(500);
//}

void turn180() {
p.setMotorTargets(0,0,-360,3350);
delay(4000);
p.resetEncoders();
}
