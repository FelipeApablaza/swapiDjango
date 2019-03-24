from django.shortcuts import render
from django.http import HttpResponse
import requests

url='https://swapi.co/api/'
def myView(request):
    return HttpResponse("Hello World")

def homeView(request):
    r = requests.get(url+'films/')
    r = r.json()
    num= r['count']
    res= r['results']

    roman={1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII'}
    dicc={'films':[]}
    for i in range (num):
        dicc['films'].append({'title':res[i]['title'],'date':res[i]['release_date'][0:4],'director':res[i]['director']
        ,'producer':res[i]['producer'],'episode':roman[res[i]['episode_id']]})

    dicc['films'].sort(key=lambda x:x['episode'])
    return render(request,'home.html',dicc)
