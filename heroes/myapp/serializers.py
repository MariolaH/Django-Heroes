from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Hero
from .models import AbilityType
from .models import Ability


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        # list of fields you want to see on the front end
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class AbilityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbilityType
        fields = ['id', 'name']

class AbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ability
        # fields = ['id', 'abilitytype_id', 'heroes_id']
        fields='__all__'

class HeroSerializer(serializers.ModelSerializer):
    abilitytype = AbilityTypeSerializer(required=False)
    class Meta:
        model = Hero
        fields = ['id', 'name', 'about_me', 'biography', 'abilitytype']