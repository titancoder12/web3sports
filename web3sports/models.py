from django.db import models
from django.forms import ValidationError

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




class Game(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(blank=True)
    time = models.TimeField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="home_games", blank=True, null=True)
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="away_games", blank=True, null=True)
    league = models.ForeignKey(League, on_delete=models.SET_NULL, related_name="games", null=True, blank=True)
    is_verified = models.BooleanField(default=False)  # True if manually verified

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

class GameLineupEntry(models.Model):
    POSITION_CHOICES = [
        ('P', 'Pitcher'),
        ('C', 'Catcher'),
        ('1B', 'First Base'),
        ('2B', 'Second Base'),
        ('3B', 'Third Base'),
        ('SS', 'Shortstop'),
        ('LF', 'Left Field'),
        ('CF', 'Center Field'),
        ('RF', 'Right Field'),
        ('DH', 'Designated Hitter'),
    ]

    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="lineup_entries")
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    position = models.CharField(max_length=20, choices=POSITION_CHOICES)

    # Ensures lineup order
    lineup_order = models.PositiveIntegerField()

    # Differentiates home & away team
    home_team = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="home_lineup_entries", null=True, blank=True)
    away_team = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="away_lineup_entries", null=True, blank=True)

    class Meta:
        unique_together = ('game', 'player', 'home_team', 'away_team')  # Prevents duplicate entries
        ordering = ['lineup_order']  # Ensures ordered retrieval

    def clean(self):
        if self.home_team and self.away_team:
            raise ValidationError("A lineup entry cannot belong to both home and away teams.")
        if not self.home_team and not self.away_team:
            raise ValidationError("A lineup entry must belong to either the home or away team.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        team_type = "Home" if self.home_team else "Away"
        return f"{self.player.name} - {self.position} ({team_type}, Order {self.lineup_order}) in {self.game.name}"
