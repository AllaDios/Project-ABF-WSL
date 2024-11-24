import serial
import time

# Configuración de la conexión serial
arduino_port = "/dev/ttyUSB0"  # O usa el puerto adecuado
baud_rate = 9600
ser = serial.Serial(arduino_port, baud_rate, timeout=1)

def read_sensors():
    try:
        line = ser.readline().decode("utf-8").strip()
        if line:
            print(f"Raw data: {line}")  # Mostrar los datos crudos para depuración
            data = {}
            # Verificar que la línea contiene al menos un par clave-valor
            if ',' in line:
                for pair in line.split(","):
                    # Asegurarse de que la línea tiene exactamente dos valores (clave y valor)
                    if ':' in pair:
                        key, value = pair.split(":", 1)
                        # Solo intentamos convertir a int si el valor es numérico
                        if value.isdigit():
                            data[key] = int(value)
                        else:
                            data[key] = value  # Si no es numérico, lo dejamos como texto
            return data
    except Exception as e:
        print(f"Error leyendo datos: {e}")
        return None

def send_command(command):
    """
    Envía un comando al Arduino.
    """
    ser.write(f"{command}\n".encode("utf-8"))
    time.sleep(1)  # Esperar a que el Arduino procese el comando
    response = ser.readline().decode("utf-8").strip()
    return response

def main():
    print("Conectando al Arduino...")
    time.sleep(2)  # Esperar a que Arduino se inicialice

    while True:
        # Leer datos de los sensores
        sensor_data = read_sensors()
        if sensor_data:
            print("Datos del invernadero:")
            print(f"  Humedad del suelo: {sensor_data.get('SOIL', 'No disponible')}")
            print(f"  Nivel de luz: {sensor_data.get('LIGHT', 'No disponible')}")
            print(f"  Nivel de agua: {sensor_data.get('WATER', 'No disponible')}")
            print(f"  Estado: {sensor_data.get('STATUS', 'No disponible')}")

            # Lógica básica para controlar el flujo de agua
            if 'SOIL' in sensor_data and sensor_data['SOIL'] < 500:  # Si la humedad del suelo es baja
                print("Humedad baja, abriendo flujo de agua...")
                response = send_command("OPEN_FLOW")
                print(f"Arduino: {response}")
            elif 'SOIL' in sensor_data and sensor_data['SOIL'] > 800:  # Si la humedad es alta
                print("Humedad alta, cerrando flujo de agua...")
                response = send_command("CLOSE_FLOW")
                print(f"Arduino: {response}")

            print("\n---\n")
        time.sleep(2)

if __name__ == "__main__":
    main()
