int r_motor_pwm = 10;  //PWM control Right Motor -
int l_motor_pwm = 11;  //PWM control Right Motor +

int r_dir = 12;   //PWM control Left Motor +
int l_dir = 13;   //PWM control Left Motor -
int incomingByte = 0;	// for incoming serial data


void setup()
{
  pinMode(r_motor_pwm, OUTPUT);  //Set control pins to be outputs
  pinMode(l_motor_pwm, OUTPUT);
  pinMode(r_dir, OUTPUT);
  pinMode(l_dir, OUTPUT);
  
  digitalWrite(r_motor_pwm, LOW);  //set both motors off for start-up
  digitalWrite(l_motor_pwm, LOW);
  digitalWrite(r_dir, LOW);
  digitalWrite(l_dir, LOW);

  
  Serial.begin(115200);   
  
  Serial.print("Enter keys -- f , b , r , l , s for drive control \n");
  Serial.print("f = Forward \n");
  Serial.print("b = Backward \n");
  Serial.print("r = Right \n");
  Serial.print("l = Left \n");
  Serial.print("s = Stop  \n");
  Serial.print("Zagros Robotics, Inc.");
}

void loop()
{

 
       
  
  	if (Serial.available() > 0) {
		// read the incoming byte:
		incomingByte = Serial.read();
		}

  
  
  
  switch(incomingByte)
  {
     case 's':
       digitalWrite(r_motor_pwm, LOW);  //Set motor direction, 1 low, 2 high
       digitalWrite(l_motor_pwm, LOW);
       digitalWrite(r_dir, LOW);  
       digitalWrite(l_dir, LOW);
       Serial.println("Stoping\n");
       incomingByte='*';
      
     break;
     
     case 'f':
       digitalWrite(r_dir, LOW);  //Set motor direction, 1 low, 2 high
       analogWrite(r_motor_pwm, 190);
       digitalWrite(l_dir, HIGH);  
       analogWrite(l_motor_pwm, 190);
       Serial.println("Moving Forward\n");
       incomingByte='*';
     break;
    
      case 'b':
        digitalWrite(r_dir, HIGH);  //Set motor direction, 1 low, 2 high
       analogWrite(r_motor_pwm, 190);
       digitalWrite(l_dir, LOW);  
       analogWrite(l_motor_pwm, 190);
       Serial.println("Moving Backwards\n");
       incomingByte='*';
     break;
     
     case 'l':
       digitalWrite(r_dir, HIGH);  //Set motor direction, 1 low, 2 high
       analogWrite(r_motor_pwm, 190);
       digitalWrite(l_dir, HIGH);
       analogWrite(l_motor_pwm, 190);  
       Serial.println("Rotating Left\n");
       incomingByte='*';
     break;

     
       case 'r':
      digitalWrite(r_dir, LOW);  //Set motor direction, 1 low, 2 high
       analogWrite(r_motor_pwm, 190);
       digitalWrite(l_dir, LOW);
       analogWrite(l_motor_pwm, 190);  
       Serial.println("Rotating Right\n");
       incomingByte='*';
     break;
     
     case 'v':
     Serial.print("MiniBot Version 8/4/2012 ");
     Serial.println();
     Serial.print("Zagros Robotics, Inc.");
     incomingByte='*';
     break;
     
    delay(5000);
   
  }
  
 
            
  
}  

