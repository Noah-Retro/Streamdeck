void setup() {
  pinMode(13, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:

  digitalWrite(13, HIGH);
  delay(500);
  digitalWrite(13, LOW);
  delay(500);
}
