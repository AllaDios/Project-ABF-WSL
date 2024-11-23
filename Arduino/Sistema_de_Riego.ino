const int relayPin = 3;   // Relé 
const int sensorHumPin = A1;  // Higrómetro
const int waterLevelPin = A0;  // Sensor de nivel de agua

int sensorHumValue = 0;  //Variable del higrómetro
int waterLevelValue = 0; //Nivel de agua
int thresholdHumidity = 600;  // Umbral de humedad
int thresholdWaterLevel = 300;  // Umbral de nivel de agua

void setup() {
  pinMode(relayPin, OUTPUT); 
  digitalWrite(relayPin, LOW); 

  Serial.begin(9600); 
}

void loop() {
  // Lee el valor del higrómetro
  sensorHumValue = analogRead(sensorHumPin);
  // Lee el valor del sensor de nivel de agua
  waterLevelValue = analogRead(waterLevelPin);

  // Se imprime los valores de humedad y nivel de agua
  Serial.print("Valor del higrómetro: ");
  Serial.print(sensorHumValue);
  Serial.print("\tValor del nivel de agua: ");
  Serial.println(waterLevelValue);

  // Se verifica si el nivel de agua es suficiente
  if (waterLevelValue > thresholdWaterLevel) {
    // Si la humedad es baja y el nivel de agua es suficiente, enciende la bomba
    if (sensorHumValue > thresholdHumidity) {
      digitalWrite(relayPin, HIGH);  // Enciende la bomba
      Serial.println("Bomba encendida (suelo seco y suficiente agua)");
    } else {
      digitalWrite(relayPin, LOW);  // Apaga la bomba si el suelo está húmedo
      Serial.println("Bomba apagada (suelo húmedo)");
    }
  } else {
    // Si el nivel de agua es bajo, apaga la bomba
    digitalWrite(relayPin, LOW);  
    Serial.println("Nivel de agua bajo, bomba apagada");
  }

  delay(4000);  // Repetición cada 4 segundos
}
