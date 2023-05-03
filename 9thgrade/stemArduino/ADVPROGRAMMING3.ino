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
while(p.readLineSensor(4) < 1){
  p.setMotorPowers(20,20);
  }
  p.setMotorPowers(125,125);

 for(int x=0;x<=1000; x++){
  followLine();
  stopAtObstacle();

  }

  }

void followLine() {
  if(p.readLineSensor(4) == 0){p.setMotorPowers(125,10);}
  else if(p.readLineSensor(4) == 1){p.setMotorPowers(10,125);}

  }

void stopAtObstacle(){
   if(p.readSonicSensorCM(5) < 25){
  p.setMotorPowers(125,125);
  delay(2000);
  }
}

void followLines(){
  
  }
