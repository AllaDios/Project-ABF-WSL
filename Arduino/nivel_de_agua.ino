// Definir el pin analógico al que está conectado el sensor de agua
const int waterSensorPin = A0;

// Variables para almacenar los valores de lectura
int waterLevel = 0;

void setup() {
  // Inicializar la comunicación serial
  Serial.begin(9600);
}

void loop() {
  // Leer el valor analógico del sensor de agua
  waterLevel = analogRead(waterSensorPin);

  // Convertir la lectura a un porcentaje (0-100%)
  int waterPercentage = map(waterLevel, 500, 720, 0, 100);

  // Asegurarse de que el porcentaje no sea menor a 0 o mayor a 100
  waterPercentage = constrain(waterPercentage, 0, 100);

  // Imprimir los resultados en el monitor serial
  Serial.print("Lectura del sensor: ");
  Serial.print(waterLevel);
  Serial.print(" | Nivel de agua: ");
  Serial.print(waterPercentage);
  Serial.println("%");

  // Esperar un segundo antes de la próxima lectura
  delay(1000);
}