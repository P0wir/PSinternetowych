from rest_framework import serializers
from .models import Schedule
from teams.serializers import TeamsSerializer

class ScheduleSerializer(serializers.ModelSerializer):
    team_home = serializers.CharField(source="team_home.team_name", read_only=True)
    team_away = serializers.CharField(source="team_away.team_name", read_only=True)
    class Meta:
        model = Schedule
        fields = (
            'team_home',
            'team_away',
            'location',
            'date',
            'time'
        )

