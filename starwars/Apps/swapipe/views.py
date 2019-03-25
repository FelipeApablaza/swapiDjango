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
    return render(request,'planet.php')

def characterView(request,num):
    return render(request,'character.php')

def starshipView(request,num):
    return render(request,'starship.php')
