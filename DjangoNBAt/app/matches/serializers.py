from rest_framework import serializers
from .models import Matches
from teams.serializers import TeamsSerializer

class MatchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matches
        fields = (
            'id',
            'team_home',
            'team_away',
            'score_home',
            'score_away',
            'location',
            'date',
            'time'
        )

