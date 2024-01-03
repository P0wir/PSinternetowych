from rest_framework import serializers
from .models import Schedule
from teams.serializers import TeamsSerializer

class ScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Schedule
        fields = ('team_home',
                  'team_away',
                  'location',
                  'date',
                  'time')
