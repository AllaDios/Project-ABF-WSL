const int ldrPin = A0;        // Pin analógico para la fotorresistencia
const int potPin = A1;        // Pin analógico para el potenciómetro
const int tempPin = A2;       // Pin analógico para el sensor de temperatura
const int bombaPin = 8;       // Pin digital para controlar el LED de la bomba

// Pines digitales para los LEDs de nivel de agua
const int ledNivel1 = 9;
const int ledNivel2 = 10;
const int ledNivel3 = 11;
const int ledNivel4 = 12;

const int umbralHumedad = 300; // Umbral de humedad para activar la bomba
int nivelAgua = 4;             // Nivel de agua inicial (4 = lleno)

void setup() {
  Serial.begin(9600);         // Iniciar la comunicación serial
  pinMode(bombaPin, OUTPUT);  // Configurar el pin del LED de la bomba como salida

  // Configurar los LEDs de nivel como salidas
  pinMode(ledNivel1, OUTPUT);
  pinMode(ledNivel2, OUTPUT);
  pinMode(ledNivel3, OUTPUT);
  pinMode(ledNivel4, OUTPUT);

  Serial.println("Iniciando lectura de sensores...");
}

void loop() {
  // Leer el valor de la fotorresistencia
  int ldrValue = analogRead(ldrPin);
  Serial.print("Luz (LDR): ");
  Serial.print(ldrValue);
  Serial.print(" | ");

  // Leer el valor del potenciómetro (simula humedad)
  int potValue = analogRead(potPin);
  Serial.print("Humedad (Potenciometro): ");
  Serial.print(potValue);
  Serial.print(" | ");

  // Leer el valor del sensor de temperatura
  int tempValue = analogRead(tempPin);
  float voltage = tempValue * (5.0 / 1023.0);  // Convertir a voltaje
  float temperatureC = (voltage - 0.5) * 100;  // Convertir a grados Celsius
  Serial.print("Temperatura (C): ");
  Serial.println(temperatureC);

  // Control de la bomba y nivel de agua
  if (potValue < umbralHumedad && nivelAgua > 0) {
    digitalWrite(bombaPin, HIGH);  // Encender la bomba
    Serial.println("Bomba activada: Riego en progreso...");
    nivelAgua--;  // Reducir nivel de agua
  } else if (nivelAgua == 0) {
    digitalWrite(bombaPin, LOW);  // Apagar la bomba si no hay agua
    Serial.println("Nivel de agua agotado: Riego no disponible.");
  } else {
    digitalWrite(bombaPin, LOW);  // Apagar la bomba si hay suficiente humedad
    Serial.println("Bomba desactivada: Humedad suficiente.");
  }

  // Actualizar LEDs del nivel de agua
  actualizarNivelAgua();
  delay(1000);  // Esperar 1 segundo antes de la siguiente iteración
}

// Función para actualizar los LEDs según el nivel de agua
void actualizarNivelAgua() {
  // Array de pines de LEDs
  int ledPins[] = {ledNivel1, ledNivel2, ledNivel3, ledNivel4};

  // Actualizar estado de los LEDs
  for (int i = 0; i < 4; i++) {
    digitalWrite(ledPins[i], (i < nivelAgua) ? HIGH : LOW);
  }

  // Mostrar estado en el monitor serial
  Serial.print("Nivel de agua: ");
  Serial.println(nivelAgua);
}# Introducción

