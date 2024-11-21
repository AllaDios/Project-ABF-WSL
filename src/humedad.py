# archivo: humedad.py
import requests

def obtener_humedad():
    api_key = "643288946356458d973114056242111"
    ciudad = "Cordoba,AR"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={ciudad}&aqi=no"

    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Lanza una excepción si la respuesta tiene un código de error
        datos = respuesta.json()
        # Extraer la humedad
        humedad = datos.get("current", {}).get("humidity")
        if humedad is not None:
            return f"{humedad}% "
        else:
            print("No se encontró el dato de humedad en la respuesta.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
        return None



humedad = obtener_humedad()
print(humedad)