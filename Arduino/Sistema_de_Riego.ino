const int relayPin = 3;       // Pin para el relé
const int sensorHumPin = A1;  // Pin para el sensor de humedad (higrómetro)
const int waterLevelPin = A0; // Pin para el sensor de nivel de agua
const int sensorLuzPin = A2;  // Pin para el sensor de luz (LDR)

int sensorHumValue = 0;       // Variable para el valor del higrómetro
int waterLevelValue = 0;      // Variable para el valor del nivel de agua
int sensorLuzValue = 0;       // Variable para el valor del sensor de luz
int thresholdHumidity = 600;  // Umbral para la humedad del suelo
int thresholdWaterLevel = 300; // Umbral para el nivel de agua

void setup() {
  pinMode(relayPin, OUTPUT); 
  digitalWrite(relayPin, LOW); // Apagar la bomba por defecto

  Serial.begin(9600);  // Iniciar la comunicación serial
}

void loop() {
  // Leer el valor del sensor de humedad
  sensorHumValue = analogRead(sensorHumPin);

  // Leer el valor del sensor de nivel de agua
  waterLevelValue = analogRead(waterLevelPin);

  // Leer el valor del sensor de luz (LDR)
  sensorLuzValue = analogRead(sensorLuzPin);

  // Enviar los datos en el formato esperado: clave:valor
  Serial.print("SOIL:");
  Serial.print(sensorHumValue);  // Humedad del suelo
  Serial.print(",LIGHT:");
  Serial.print(sensorLuzValue);  // Valor de luz
  Serial.print(",WATER:");
  Serial.print(waterLevelValue);  // Nivel de agua

  // Control de la bomba basado en el nivel de agua y humedad
  if (waterLevelValue > thresholdWaterLevel) {
    if (sensorHumValue > thresholdHumidity) {
      digitalWrite(relayPin, HIGH);  // Enciende la bomba
      Serial.print(",STATUS:ON");  // Bomba encendida
    } else {
      digitalWrite(relayPin, LOW);  // Apaga la bomba si el suelo está húmedo
      Serial.print(",STATUS:OFF");  // Bomba apagada
    }
  } else {
    digitalWrite(relayPin, LOW);  // Apaga la bomba si el nivel de agua es bajo
    Serial.print(",STATUS:OFF");  // Bomba apagada
  }

  // Enviar los datos con formato 'clave:valor' por cada parámetro
  Serial.println();  // Nueva línea para terminar la transmisión de datos
  delay(2000);  // Espera 2 segundos antes de la siguiente lectura
}
