from django.db import models


class Teams(models.Model):
    team_name = models.CharField(max_length=256, unique=True)
    year = models.FloatField()
    city = models.CharField(max_length=255)
    conference = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.team_name}"
