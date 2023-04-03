from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Hero
from .models import AbilityType
from .models import Ability
from .models import Relationship
from .models import RelationshipTypes

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
        fields = ['name']

class AbilitySerializer(serializers.ModelSerializer):
    # ability = AbilitySerializer(many=True)
    class Meta:
        model = Ability
        # fields = ['id', 'abilitytype_id', 'heroes_id']
        fields='__all__'

class RelationshipTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelationshipTypes
        fields=['name']
                

class HeroSerializer(serializers.ModelSerializer):
    relationshiptype = RelationshipTypesSerializer(many=True)
    abilitytype = AbilityTypeSerializer(many=True)
    class Meta:
        model = Hero
        fields = ['id', 'name', 'about_me', 'biography', 'abilitytype', 'hero1', 'relationshiptype']

class RelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relationship
        fields='__all__'

