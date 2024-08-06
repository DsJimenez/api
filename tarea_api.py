# Importacion de bibioteca para interactuar la API
import requests

# Guardamos la URL para hacer la solicitud. 
url = "https://api.lambdatest.com/automation/api/v1/platforms"

# Guardamos la respuesta.
respuesta = requests.get(url)

# Creamos un bucle para 
if respuesta.status_code == 200:
    print("Solicitud Exitosa.")
    print("Datos:",respuesta.json())
else:
    print("Error en la solicitud del recurso. Detalles: \n",
          respuesta.text)