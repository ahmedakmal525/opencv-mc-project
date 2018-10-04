#include <Servo.h>

Servo myservo;
int pos = 60;
char msg = " ";

void setup()
{
    myservo.attach(9);
    Serial.begin(9600);
    Serial.print("Program Initiated");    	
    pinMode(2,OUTPUT); // 5V for servo    	
    pinMode(12,OUTPUT); // Pulse Width Modulation for motor
    Serial.flush();
}

void loop() {
    digitalWrite(12, HIGH);
    while (Serial.available() > 0) {
        msg = Serial.read();
    }
    myservo.write(120);
    delay(1000);
    if (msg == "Y") {    
        digitalWrite(12,LOW);      
        delay(1200);    
        for (pos = 120; pos >=50; pos -= 2){              
            myservo.write(pos);                          
            delay(5);       
        }       
        for (pos = 53; pos <=120; pos += 2){
            myservo.write(pos);
        }
    delay(5);
    digitalWrite(12, HIGH);
    msg = " ";
    Serial.flush();
    } else if (msg == "N") {
        for (pos = 120; pos >55; pos -= 2) {         	 	
            myservo.write(pos);                    	 	 
            delay(10);
        }
        msg = " ";
        Serial.flush();
    }
}
