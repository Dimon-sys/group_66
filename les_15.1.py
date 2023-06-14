import requests
import json

url = 'http://swapi.dev/api/'

responce = requests.get(url).json()

people_api = responce.get('people')
planets_api = responce.get('planets')
starships_api = responce.get('starships')

def check_people(url):
    for i in range(1, 6):
        responce = requests.get(f'{url}/{i}').json()
        print(responce)

#check_people(people_api)

def check_planets(url):
    diameters_list = []
    for i in range(1, 6):
        responce = requests.get(f'{url}/{i}').json()
        diameters_list.append({responce.get('name') : responce.get('diameter')})
    print(diameters_list)

def max_speed(url):
    max_speed_list = []
    for i in range(1, 11):
        responce = requests.get(f'{url}/{i}').json()
        max_speed_list.append(int(responce.get('max_atmosphering_speed')))
    print(max(max_speed_list))

def max_diameter(url):
    diameters_list = []
    for i in range(1, 11):
        responce = requests.get(f'{url}/{i}').json()
        diameters_list.append(int(responce.get('diameter')))
    print(max(diameters_list))


max_speed(starships_api)