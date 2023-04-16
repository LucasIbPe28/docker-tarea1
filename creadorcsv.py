import csv
import requests


url = "https://api.spacexdata.com/v4/launches"
respuesta = requests.get(url)
datos_api = respuesta.json()


with open("lanzamientos_spacex.csv", "w", newline="") as archivo_csv:
    campos = ["id", "nombre", "fecha", "exitoso", "nave"]
    escritor_csv = csv.DictWriter(archivo_csv, fieldnames=campos)

    escritor_csv.writeheader()

    for lanzamiento in datos_api:
        id_lanzamiento = lanzamiento["id"]
        nombre = lanzamiento["name"]
        fecha = lanzamiento["date_utc"]
        exitoso = lanzamiento["success"]

        escritor_csv.writerow({"id": id_lanzamiento, "nombre": nombre, "fecha": fecha, "exitoso": exitoso})