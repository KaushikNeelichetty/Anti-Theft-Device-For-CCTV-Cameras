/**
 *
 * @author Srinivasan,Kaushik,Prabhakar,Aditthya,Sanjay
 */
#include <SoftwareSerial.h> // to make Digital pins act as Tx and Rx pins
int WireCut=A5;//WIRE CUT INPUT
int ledBuzz=5;//OUTPUT ALARM
int senRead=A0;//IR INPUT         
SoftwareSerial mySerial(9, 10);//Rx And Tx pins for GSM Module

void setup()    
 {
  /* This function runs only once and is used to setup the Arduino */
  pinMode(WireCut,INPUT);
  pinMode(ledBuzz,OUTPUT);
  pinMode(senRead,INPUT);
  Serial.begin(19200);//Setting the serial port at baud rate of 19200
  mySerial.begin(19200);//Software Serial and Serial has to have same Baud Rate
}  

void SMS(){
  /*This Function sends an SMS to the specified Number*/
  mySerial.println("AT+CMGF=1");    //Sets the GSM Module in Text Mode
  delay(1000);  // Delay of 1000 milli seconds or 1 second
  mySerial.println("AT+CMGS=\"+91xxxxxxxxxx\"\r"); // AT command for Sending an SMS
  delay(1000);
  mySerial.println("CAMERA THEFT!!!");// The SMS text you want to send
  delay(100);
  mySerial.println((char)26);// ASCII code of CTRL+Z
  delay(10000);
  
}
void CALL(){
  /*This Function calls the specified number*/
     mySerial.println("ATD + +91xxxxxxxxxx;"); //AT Command to make calls
     delay(100);
     mySerial.println();
     delay(60000);//Wait for One minute before hanging up
     mySerial.println("ATH");//Hang Up the call
}
void loop(){
  /*This code runs continously*/
  int i=0;//index for loop  
  int IR=analogRead(senRead);//Read the value from the IR Sensor 
  int WC;
  WC=analogRead(WireCut);//Read the value from the wire cut
  Serial.println("Wire cut reads "+WC);
  Serial.println("IR Photodiode reads "+IR);
  delay(1000);//Wait for a second...
  if(IR>800 || WC<1000){//Condition for alarm
     digitalWrite(ledBuzz,HIGH);//Send HIGH value to the LED and BUZZER
     SMS();//Send the alert SMS     
     for(;i<3;i++){//Make 3 calls
      CALL();//Call the concerned authority
     }
  }
  else{
  digitalWrite(ledBuzz,LOW);//Keep the LED and Buzzer turned off.
  }
}

