from django.db import models
from schedule.models import Schedule
from teams.models import Teams
from django.contrib.auth.models import User

class Bet(models.Model):
    match = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name='bet_on_match')
    selected_team = models.ForeignKey(Teams, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.selected_team} in {self.match}"

    class Meta:
        verbose_name = "Bet"
        verbose_name_plural = "Bets"


class Odds(models.Model):
    match = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
    odds_value = models.FloatField()

    def __str__(self):
        return f"{self.match} - {self.team} - {self.odds_value}"

    class Meta:
        verbose_name = "Odds"
        verbose_name_plural = "Odds"