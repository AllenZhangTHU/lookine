#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// a maximum of eight servo objects can be created

#define servo_pin SDA

String inString = "";

int pos = 0;    // variable to store the servo position

void setup()
{
  Serial.begin(9600);
  myservo.attach(servo_pin);  // attaches the servo on pin 9 to the servo object
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }
  pos = 90;
  myservo.write(pos);
}


void loop()
{
  while (Serial.available() > 0)
  {
    inString += char(Serial.read());
    delay(2);
  }
  if (inString.length() > 0)
  {
    pos = pos + inString.toInt();
    myservo.write(pos);
    Serial.println(pos);
  }
  inString = "";
}
