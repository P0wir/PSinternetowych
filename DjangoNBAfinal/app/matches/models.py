from django.db import models
from teams.models import Teams

class Matches(models.Model):
    team_home = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='home_matches')
    team_away = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='away_matches')
    score_home = models.IntegerField()
    score_away = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.team_home} vs {self.team_away} {self.score_home}:{self.score_away} {self.date}"

    class Meta:
        verbose_name = "Match"
        verbose_name_plural = "Matches"
