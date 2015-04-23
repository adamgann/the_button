// Light LEDs based on serial values received. Host-side PC gets data
// from r/thebutton

// Variable to store received serial data
int inByte = 0;

// Define colors
int purple = 2;
int blue = 3;
int green = 4;
int yellow = 5;
int orange = 6;
int red = 7;

void setup()  
{
  // Open serial communications and wait for port to open:
  Serial.begin(57600);
  while (!Serial) 
  {
  }
  Serial.println("Serial Connection is Good");
  
  //Set up pins
  for (int ii=purple;ii<=red;ii++)
  {  
    pinMode(ii, OUTPUT);
    digitalWrite(ii, LOW); 
  }

}

void loop() // run over and over
{
    if (Serial.available() > 0) 
    {
      // get incoming byte:
      inByte = Serial.read()-'0';
      setColor(inByte);
    }
}

void setColor(int color)
{
  // Make sure color value is within acceptable range
  if (color>red)
  {
    return;
  }
  if (color<purple)
  {
    return;
  }
    
  // Turn off all other colors  
  for (int ii=purple;ii<=red;ii++)
  {
    digitalWrite(ii, LOW); 
  }
  
  // Enable the chosen color
  digitalWrite(color,HIGH);
}


