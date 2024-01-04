from django.db import models
from teams.models import Teams

class Players(models.Model):
    player_name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    date_of_birth = models.DateField()
    height = models.FloatField()  # wzrost w cm
    weight = models.FloatField()  # waga w kg
    team = models.ForeignKey(Teams, on_delete=models.CASCADE, to_field='team_name')

    def __str__(self):
        return f"{self.player_name} {self.surname}"

    class Meta:
        verbose_name = "Player"
        verbose_name_plural = "Players"
