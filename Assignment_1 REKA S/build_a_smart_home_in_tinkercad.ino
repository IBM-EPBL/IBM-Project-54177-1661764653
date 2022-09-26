// C++ code
//
void setup()
{
  pinMode(13,OUTPUT);
  pinMode(12,OUTPUT);
  Serial.begin(7000);
}

void loop()
{
  digitalWrite(13, HIGH);
  Serial.println("13LED ON");
  digitalWrite(12,OUTPUT);
  Serial.println("12LED ON");
}