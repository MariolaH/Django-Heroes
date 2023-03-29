from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import *

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>The time is now %s.</body></html>" % now
    return HttpResponse(html)

# def book_getter(request, book_id):
#     print(book_id)
#     return HttpResponse('<h1>hello!!!</h1>')

# def get_hero(request, hero_id):
#     print(hero_id)
#     selected_hero = Hero.objects.get(pk=hero_id)
#     print(selected_hero)
#     return HttpResponse('<h1>HERO: %s </h1>' % selected_hero.name)

def get_hero(request):
    # print(hero_id)
    selected_hero = Hero.objects.values_list('name', 'about_me', 'biography')
    # print(selected_hero)
    html = ''
    for name in selected_hero:
        html += ''' <h1>Hero: %s <p> About me: %s</p> <p>Bio: %s </p></h1> ''' % name
    return HttpResponse(html)

