# archivo: humedad.py
import requests

def obtener_temperatura():
    api_key = "643288946356458d973114056242111"
    ciudad = "Cordoba,AR"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={ciudad}&aqi=no"

    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Lanza una excepción si la respuesta tiene un código de error
        datos = respuesta.json()
        # Extraer la temperatura
        temperatura = datos.get("current", {}).get("temp_c")
        if temperatura is not None:
            return f"{temperatura}° "
        else:
            print("No se encontró el dato de temperatura en la respuesta.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
        return None



temperatura = obtener_temperatura()
print(temperatura)