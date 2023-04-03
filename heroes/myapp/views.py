from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Hero
from .models import AbilityType
from .models import Ability
from .models import Relationship
from .models import RelationshipTypes

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, HeroSerializer, AbilityTypeSerializer, AbilitySerializer, RelationshipSerializer, RelationshipTypesSerializer


# UserViewSet is the model we want to steralizqe

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer

class AbilityTypeViewSet(viewsets.ModelViewSet):
    queryset = AbilityType.objects.all()
    serializer_class = AbilityTypeSerializer

class AbilityViewSet(viewsets.ModelViewSet):
    queryset = Ability.objects.all()
    serializer_class = AbilitySerializer

class RelationshipViewSet(viewsets.ModelViewSet):
    queryset = Relationship.objects.all()
    serializer_class = RelationshipSerializer

class RelationshipTypesViewSet(viewsets.ModelViewSet):
    queryset = RelationshipTypes.objects.all()
    serializer_class = RelationshipTypesSerializer

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

