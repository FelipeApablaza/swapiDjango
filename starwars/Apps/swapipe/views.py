from django.shortcuts import render
from django.http import HttpResponse
import requests

url='https://swapi.co/api/'


def homeView(request):
    r = requests.get(url+'films/')
    r = r.json()
    num= r['count']
    res= r['results']
    roman={1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII'}
    dicc={'films':[]}
    for i in range (num):
        dicc['films'].append({'title':res[i]['title'],'date':res[i]['release_date'][0:4],'director':res[i]['director']
        ,'producer':res[i]['producer'],'episode':roman[res[i]['episode_id']],'id':res[i]['url'].split('/')[-2]})

    dicc['films'].sort(key=lambda x:x['date'])
    return render(request,'home.php',dicc)

def filmView(request,num):
    r = requests.get(url+"films/"+num)
    r = r.json()

    dicc={'film':[{'title':r['title'],'episode':r['episode_id'],'opening':r['opening_crawl'],'director':r['director'],'producer':r['producer'],'date':r['release_date'],'starships':[],'planets':[],'characters':[]}]}

    for x in r['starships']:
        res=requests.get(x)
        res=res.json()
        dicc['film'][0]['starships'].append({'name':res['name'],'id':res['url'].split('/')[-2]})

    for y in r['planets']:
        res=requests.get(y)
        res=res.json()
        dicc['film'][0]['planets'].append({'name':res['name'],'id':res['url'].split('/')[-2]})

    for z in r['characters']:
        res=requests.get(z)
        res=res.json()
        dicc['film'][0]['characters'].append({'name':res['name'],'id':res['url'].split('/')[-2]})

    return render(request,'film.php',dicc)

def planetView(request,num):
    r = requests.get(url+"planets/"+num)
    r = r.json()

    dicc={'planet':[{'name':r['name'],'rotation_period':r['rotation_period'],'orbital_period':r['orbital_period'],'diameter':r['diameter'],'climate':r['climate'],'gravity':r['gravity'],'terrain':r['terrain'],'surface_water':r['surface_water'],'population':r['population'],'residents':[],'films':[]}]}
    for x in r['residents']:
        res=requests.get(x)
        res=res.json()
        dicc['planet'][0]['residents'].append({'name':res['name'],'id':res['url'].split('/')[-2]})

    for y in r['films']:
        res=requests.get(y)
        res=res.json()
        dicc['planet'][0]['films'].append({'title':res['title'],'id':res['url'].split('/')[-2]})

    return render(request,'planet.php',dicc)

def characterView(request,num):
    r = requests.get(url+"people/"+num)
    r = r.json()

    dicc={'character':[{'name':r['name'],'height':r['height'],'mass':r['mass'],'hair_color':r['hair_color'],'skin_color':r['skin_color'],'eye_color':r['eye_color'],'birth_year':r['birth_year'],'gender':r['gender'],'homeworld':'','films':[],'starships':[]}]}
    for x in r['starships']:
        res=requests.get(x)
        res=res.json()
        dicc['character'][0]['starships'].append({'name':res['name'],'id':res['url'].split('/')[-2]})

    for y in r['films']:
        res=requests.get(y)
        res=res.json()
        dicc['character'][0]['films'].append({'title':res['title'],'id':res['url'].split('/')[-2]})

    z = r['homeworld']
    res = requests.get(z)
    res = res.json()
    dicc['character'][0]['homeworld']=[{'name':res['name'],'id':res['url'].split('/')[-2]}]
    return render(request,'character.php',dicc)

def starshipView(request,num):
    r = requests.get(url+"starships/"+num)
    r = r.json()

    dicc={'starship':[{'name':r['name'],'model':r['model'],'manufacturer':r['manufacturer'],'cost_in_credits':r['cost_in_credits'],'length':r['length'],'max_atmosphering_speed':r['max_atmosphering_speed'],'crew':r['crew'],'passengers':r['passengers'],'cargo_capacity':r['cargo_capacity'],'consumables':r['consumables'],'hyperdrive_rating':r['hyperdrive_rating'],'MGLT':r['MGLT'],'starship_class':r['starship_class'],'pilots':[],'films':[]}]}
    for x in r['pilots']:
        res=requests.get(x)
        res=res.json()
        dicc['starship'][0]['pilots'].append({'name':res['name'],'id':res['url'].split('/')[-2]})

    for y in r['films']:
        res=requests.get(y)
        res=res.json()
        dicc['starship'][0]['films'].append({'title':res['title'],'id':res['url'].split('/')[-2]})

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
