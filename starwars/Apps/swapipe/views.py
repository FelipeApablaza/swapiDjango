from django.shortcuts import render
from django.http import HttpResponse
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import requests

url='https://swapi.co/api/'
urlgql='https://swapi-graphql-integracion-t3.herokuapp.com/'

_transport = RequestsHTTPTransport(
    url=urlgql,
    use_json=True,
)
client = Client(
    transport=_transport,
    fetch_schema_from_transport=True,
)


def homeView(request):

    query = gql ('''
    {
        allFilms {
            totalCount
            edges {
                node {
                    title
                    releaseDate
                    director
                    producers
                    episodeID
                    id
                }
            }
        }
    }
    ''')

    r_graph = client.execute(query)
    r_graph = r_graph['allFilms']
    num_graph = r_graph['totalCount']
    res_graph = r_graph['edges']
    # print(res_graph)

    r = r_graph
    num = num_graph
    res = res_graph


    # r = requests.get(url+'films/')
    # r = r.json()
    # num= r['count']
    # res= r['results']
    roman={1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII'}
    dicc={'films':[]}
    for i in range (num):
        dicc['films'].append({'title':res[i]['node']['title'],'date':res[i]['node']['releaseDate'][0:4],'director':res[i]['node']['director']
        ,'episode':roman[res[i]['node']['episodeID']],'id':res[i]['node']['id']})
        strcat = ''
        for x in res[i]['node']['producers']:
            strcat +=x+', '
        dicc['films'][i].update({'producer':strcat[:-2]})


    dicc['films'].sort(key=lambda x:x['date'])
    return render(request,'home.php',dicc)

def filmView(request,num):
    command = '''
    { 
        film(id:"%s") {
            title
            episodeID
            openingCrawl
            director
            producers
            releaseDate
            starshipConnection {
                edges {
                    node {
                        name
                        id
                    }
                }
            }
            planetConnection {
                edges {
                    node {
                        name
                        id
                    }
                }
            }
            characterConnection {
                edges {
                    node {
                        name
                        id
                    }
                }
            }
        }
    }
    ''' %(num)
    query = gql ( command )

    result = client.execute(query)
    r = result['film']


    # r = requests.get(url+"films/"+num)
    # r = r.json()

    dicc={'film':[{'title':r['title'],'episode':r['episodeID'],'opening':r['openingCrawl'],'director':r['director'],'date':r['releaseDate'],'starships':[],'planets':[],'characters':[]}]}
    strcat = ''
    for w in r['producers']:
        strcat +=w+', '
    dicc['film'][0].update({'producer':strcat[:-2]})

    for x in r['starshipConnection']['edges']:
        # res=requests.get(x)
        # res=res.json()
        dicc['film'][0]['starships'].append({'name':x['node']['name'],'id':x['node']['id']})

    for y in r['planetConnection']['edges']:
        # res=requests.get(y)
        # res=res.json()
        dicc['film'][0]['planets'].append({'name':y['node']['name'],'id':y['node']['id']})

    for z in r['characterConnection']['edges']:
        # res=requests.get(z)
        # res=res.json()
        dicc['film'][0]['characters'].append({'name':z['node']['name'],'id':z['node']['id']})

    return render(request,'film.php',dicc)

def planetView(request,num):
    command = ''' 
    { 
        planet(id:"%s") {
            name
            rotationPeriod
            orbitalPeriod
            diameter
            climates
            gravity
            terrains
            surfaceWater
            population
            residentConnection {
                edges {
                    node {
                        name
                        id
                    }
                }
            }
            filmConnection {
                edges {
                    node {
                        title
                        id
                    }
                }
            }
        }
    }
    ''' %(num)
    query = gql ( command )

    result = client.execute(query)
    r = result['planet']
    
    # r = requests.get(url+"planets/"+num)
    # r = r.json()

    dicc={'planet':[{'name':r['name'],'rotation_period':r['rotationPeriod'],'orbital_period':r['orbitalPeriod'],'diameter':r['diameter'],'gravity':r['gravity'],'surface_water':r['surfaceWater'],'population':r['population'],'residents':[],'films':[]}]}
   
    strcat1 = ''
    for w in r['climates']:
        strcat1 +=w+', '
    dicc['planet'][0].update({'climate':strcat1[:-2]})

    strcat2 = ''
    for v in r['terrains']:
        strcat2 +=v+', '
    dicc['planet'][0].update({'terrain':strcat2[:-2]})

    
    for x in r['residentConnection']['edges']:
        # res=requests.get(x)
        # res=res.json()
        dicc['planet'][0]['residents'].append({'name':x['node']['name'],'id':x['node']['id']})

    for y in r['filmConnection']['edges']:
        # res=requests.get(y)
        # res=res.json()
        dicc['planet'][0]['films'].append({'title':y['node']['title'],'id':y['node']['id']})

    return render(request,'planet.php',dicc)

def characterView(request,num):
    command = ''' 
    {
        person(id:"%s")
        {
            name
            height
            mass
            hairColor
            skinColor
            eyeColor
            birthYear
            gender
            homeworld {
                name
                id
            }
            filmConnection {
                edges {
                    node {
                        title
                        id
                    }
                }
            }
            starshipConnection {
                edges {
                    node {
                        name
                        id
                    }
                }
            }
        }
    }
    '''%(num)

    query = gql ( command )

    result = client.execute(query)
    r = result['person']
    # r = requests.get(url+"people/"+num)
    # r = r.json()

    dicc={'character':[{'name':r['name'],'height':r['height'],'mass':r['mass'],'hair_color':r['hairColor'],'skin_color':r['skinColor'],'eye_color':r['eyeColor'],'birth_year':r['birthYear'],'gender':r['gender'],'homeworld':'','films':[],'starships':[]}]}
    for x in r['starshipConnection']['edges']:
        # res=requests.get(x)
        # res=res.json()
        dicc['character'][0]['starships'].append({'name':x['node']['name'],'id':x['node']['id']})

    for y in r['filmConnection']['edges']:
        # res=requests.get(y)
        # res=res.json()
        dicc['character'][0]['films'].append({'title':y['node']['title'],'id':y['node']['id']})

    z = r['homeworld']
    # res = requests.get(z)
    # res = res.json()
    dicc['character'][0]['homeworld']=[{'name':z['name'],'id':z['id']}]
    return render(request,'character.php',dicc)

def starshipView(request,num):
    command = ''' 
    { 
        starship(id:"%s") {
            name
            model
            manufacturers
            costInCredits
            length
            maxAtmospheringSpeed
            crew
            passengers
            cargoCapacity
            consumables
            hyperdriveRating
            MGLT
            starshipClass
            pilotConnection {
                edges {
                    node {
                        name
                        id
                    }
                }
            }
            filmConnection {
                edges {
                    node {
                        title
                        id
                    }
                }
            }
        }
    }
    ''' %(num)
    query = gql ( command )

    result = client.execute(query)
    r = result['starship']
    # r = requests.get(url+"starships/"+num)
    # r = r.json()

    dicc={'starship':[{'name':r['name'],'model':r['model'],'cost_in_credits':r['costInCredits'],'length':r['length'],'max_atmosphering_speed':r['maxAtmospheringSpeed'],'crew':r['crew'],'passengers':r['passengers'],'cargo_capacity':r['cargoCapacity'],'consumables':r['consumables'],'hyperdrive_rating':r['hyperdriveRating'],'MGLT':r['MGLT'],'starship_class':r['starshipClass'],'pilots':[],'films':[]}]}
    strcat = ''
    for w in r['manufacturers']:
        strcat +=w+', '
    dicc['starship'][0].update({'manufacturer':strcat[:-2]})
    
    for x in r['pilotConnection']['edges']:
        # res=requests.get(x)
        # res=res.json()
        dicc['starship'][0]['pilots'].append({'name':x['node']['name'],'id':x['node']['id']})

    for y in r['filmConnection']['edges']:
        # res=requests.get(y)
        # res=res.json()
        dicc['starship'][0]['films'].append({'title':y['node']['title'],'id':y['node']['id']})

    return render(request,'starship.php',dicc)

def buscarFunc(request):
    var=request.GET['search']
    status=False

    res1 = buscarTodo(var,'people')
    clista={'clista':[]}
    for c in res1:
        res = requests.get(c)
        res = res.json()
        clista['clista'].append({'name':res['name'],'id':res['url'].split('/')[-2]})

    res2 = buscarTodo(var,'films')
    flista={'flista':[]}
    for f in res2:
        res = requests.get(f)
        res = res.json()
        flista['flista'].append({'title':res['title'],'id':res['url'].split('/')[-2]})

    res3 = buscarTodo(var,'starships')
    slista={'slista':[]}
    for s in res3:
        res = requests.get(s)
        res = res.json()
        slista['slista'].append({'name':res['name'],'id':res['url'].split('/')[-2]})

    res4 = buscarTodo(var,'planets')
    plista={'plista':[]}
    for p in res4:
        res = requests.get(p)
        res = res.json()
        plista['plista'].append({'name':res['name'],'id':res['url'].split('/')[-2]})

    dicc={}
    dicc.update(clista)
    dicc.update(flista)
    dicc.update(slista)
    dicc.update(plista)
    return render(request,'buscar.php',dicc)

def buscarTodo(ans,entity):
    r = requests.get(url + "{}/?search=".format(entity) + ans)
    res = r.json()
    urls = []
    next = True
    while next:
        for resource in res['results']:
            urls.append(resource['url'])
        if bool(res['next']):
            res = requests.get(res["next"]).json()
        else:
            next = False
    return urls
