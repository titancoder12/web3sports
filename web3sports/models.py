from django.db import models

# Create your models here.

class Player(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    birth_country = models.CharField(max_length=100, blank=True)
    birth_city = models.CharField(max_length=100, blank=True)
    number = models.IntegerField(null=True, blank=True)
    batting_throwing = models.CharField(max_length=10, blank=True)  # "B/T" Field
    height_weight = models.CharField(max_length=20, blank=True)  # "H/W" Field
    primary_position = models.CharField(max_length=50, blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

class League(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True, null=True)
    commissioner = models.CharField(max_length=100, blank=True)
    proof_of_legitimacy = models.TextField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)  # True if manually verified

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

class Team(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True)
    province_state = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    roster = models.ManyToManyField(Player, related_name='teams')  # Many-to-Many Relationship
    league = models.ForeignKey(League, on_delete=models.SET_NULL, related_name="teams", null=True, blank=True)  # Teams can be linked to a league
    is_approved = models.BooleanField(default=False)  # True if approved to join a league
    
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)




