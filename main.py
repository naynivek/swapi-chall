import requests
import json

initial_url = 'https://swapi.dev/api/starships/'
question_MGLT = 1000000

def get_data(url):
    r = requests.get(url)
    if r.status_code == 200:
        response = r.json()
        return response
    else:
        print('Erro de comunicação com a API: '+url)
        print('HTTP Error: '+str(r.status_code))
        return None

def converter(date):
    date = date.split(' ')
    if date[1] == 'year' or date[1] == 'years':
        return int(int(date[0]))*24*365
    elif date[1] == 'month' or date[1] == 'months':
        return int(int(date[0]))*24*30
    elif date[1] == 'week' or date[1] == 'weeks':
        return int(int(date[0]))*24*7
    elif date[1] == 'day' or date[1] == 'days':
        return int(int(date[0]))*24


result = get_data(initial_url)
spaceships = result['results']

while result['next'] is not None:
    result = get_data(result['next'])
    spaceships2 = result['results']
    for i in range(len(spaceships2)):
        spaceships.append(spaceships2[i])


for i in range(len(spaceships)):  
    if spaceships[i]['MGLT'] != 'unknown':
        hours = converter(spaceships[i]['consumables'])
        mglt_total = int(spaceships[i]['MGLT'])*hours
        stops = question_MGLT/int(mglt_total)
        print(spaceships[i]['name']+': '+str(stops))



