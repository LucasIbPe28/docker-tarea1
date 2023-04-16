#API rest

import csv
import random
import requests
import redis
import time

base_url = "https://api.spacexdata.com/v4/"
with open('lanzamientos_spacex.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    launch_names = [row for row in csv_reader]

for i in range(30):
    
    launch_name = random.choice(launch_names)
    cx=redis.Redis(host='localhost')

    if cx.hexists('historial',launch_name[1]):
        inicio = time.time()
        
        #cx.hincrby('historia',launch["name"],valoreskey)
        print('Lanzamiento de: '+launch_name[1]+'Con fecha: '+launch_name[2])
        fin=time.time()
        demora = fin-inicio
        print(f"Tiempo: {demora} ===> SI ESTABA EN REDIS")

    else:
        inicio = time.time()
        ide = launch_name[0]
        response = requests.get(base_url + "launches/" + ide)
        if response.status_code == 200:
            data = response.json()
            print(f"Nombre:"+data["name"] +",con fecha: "+data["date_utc"])
            cx.hset('historial',data["name"],data["date_utc"])
        else:
            print('Error al hacer la solicitud a la API de SpaceX.')
        
        fin=time.time()
        demora = fin-inicio
        print(f"Tiempo: {demora} ===> NO ESTABA EN REDIS")