#include <Servo.h>

// Create servo objects for 3 joints
Servo servo1;
Servo servo2;
Servo servo3;

void setup() {
  Serial.begin(9600);
  
  // Attach servos to digital PWM pins on the Arduino
  servo1.attach(9);   // Base or Joint 1
  servo2.attach(10);  // Joint 2
  servo3.attach(11);  // Joint 3
}

void loop() {
  if (Serial.available() > 0) {
    // Read the incoming string until the newline character '\n'
    String data = Serial.readStringUntil('\n');
    
    // Find the comma separators
    int firstComma = data.indexOf(',');
    int secondComma = data.indexOf(',', firstComma + 1);
    
    // Ensure valid formatting exists before parsing
    if (firstComma > 0 && secondComma > 0) {
      int angle1 = data.substring(0, firstComma).toInt();
      int angle2 = data.substring(firstComma + 1, secondComma).toInt();
      int angle3 = data.substring(secondComma + 1).toInt();
      
      // Constrain angles to prevent mechanical binding on physical hardware
      angle1 = constrain(angle1, 0, 90);
      angle2 = constrain(angle2, 0, 90);
      angle3 = constrain(angle3, 0, 90);
      
      // Command the physical servos
      servo1.write(angle1);
      servo2.write(angle2);
      servo3.write(angle3);
    }
  }
}