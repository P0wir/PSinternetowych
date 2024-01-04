from django.db import models


class Teams(models.Model):
    team_name = models.CharField(max_length=256, unique=True, primary_key=True)
    year = models.FloatField()
    city = models.CharField(max_length=255)
    conference = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.team_name}"

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"
