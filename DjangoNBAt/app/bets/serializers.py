from rest_framework import serializers
from .models import Bet, Odds
from schedule.serializers import ScheduleSerializer

class BetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bet
        fields = (
            'id',
            'match',
            'selected_team',
            'money',
            'user')

class OddsSerializer(serializers.ModelSerializer):
    match = ScheduleSerializer()
    team = serializers.CharField(source="team.team_name", read_only=True)
    class Meta:
        model = Odds
        fields = (
            'id',
            'match',
            'team',
            'odds_value')