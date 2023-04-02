from django.db import models

class Hero(models.Model):
    name = models.CharField(max_length=200)
    about_me = models.TextField()
    biography = models.TextField()
    abilitytype = models.ManyToManyField('AbilityType', through="Ability") 

class Ability(models.Model):
    heroes = models.ForeignKey('Hero', on_delete=models.CASCADE, null=True, blank=True)
    abilitytype = models.ForeignKey('AbilityType', on_delete=models.PROTECT, null=True, blank=True)
    def __str__(self):
        return self.abilitytype;   

class AbilityType(models.Model):
    name = models.CharField(max_length=200)

class RelationshipTypes(models.Model):
    name = models.CharField(max_length=200)

class Relationship(models.Model):
    hero1 = models.ForeignKey('Hero', on_delete=models.PROTECT, null= True, related_name='hero1')
    hero2 = models.ForeignKey('Hero', on_delete=models.PROTECT, null= True, related_name='hero2')
    relationshipType = models.ForeignKey('RelationshipTypes', on_delete=models.PROTECT, null=True)










