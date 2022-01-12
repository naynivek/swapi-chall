import requests
import json
from flask import Flask
from flask import request

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

app = Flask(__name__)

@app.route('/')
def ola():
    return '<h3>Flask working</h3>'

@app.route('/api', methods = ['POST', 'GET'])
def swapi():
    initial_url = 'https://swapi.dev/api/starships/'
    if request.method == 'POST':
        question_MGLT = request.form['mglt']
    else:
        question_MGLT = request.args.get('mglt', default=1000000, type = int)
    result = get_data(initial_url)
    spaceships = result['results']
    message = []

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
#            print(spaceships[i]['name']+': '+str(stops))
            message.append(spaceships[i]['name']+': '+str(stops))
    response = json.dumps(message, indent=2)
#    response = json.dumps(response, indent=10)
#    response = response.replace('\n','<br>')
    print(response)
    return response

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.run()










