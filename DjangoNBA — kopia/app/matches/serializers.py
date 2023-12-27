from rest_framework import serializers
from .models import Matches
from teams.serializers import TeamsSerializer

class MatchesSerializer(serializers.ModelSerializer):
    team_home = serializers.CharField(source="team_home.team_name", read_only=True)
    team_away = serializers.CharField(source="team_away.team_name", read_only=True)
    class Meta:
        model = Matches
        fields = (
            'team_home',
            'team_away',
            'score_home',
            'score_away',
            'location',
            'date',
            'time'
        )

