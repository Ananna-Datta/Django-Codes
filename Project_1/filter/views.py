from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    d={
        'lst' : ['a','b','c','d','e'],
        'x' : 21,
        'y' : "I'm Jai",
        'z': "jai",
        'p':"String with spaces",
        'birthday' : datetime.datetime.now(),
        'val' : '' ,
        'info':[
            {'name': 'zed', 'age': 19},
            {'name': 'amy', 'age': 22},
            {'name': 'joe', 'age': 31},
        ],
        'q':'2023-01-12T10:30:00.000123',
    }
    return render(request,'index.html',d)
