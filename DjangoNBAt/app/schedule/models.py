from django.db import models
from teams.models import Teams

class Schedule(models.Model):
    team_home = models.ForeignKey(Teams, on_delete=models.CASCADE, to_field='team_name', related_name='schedule_home_matches')
    team_away = models.ForeignKey(Teams, on_delete=models.CASCADE, to_field='team_name', related_name='schedule_away_matches')
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.team_home} vs {self.team_away} - {self.date}"

    class Meta:
        verbose_name = "Schedule"
        verbose_name_plural = "Schedule"
