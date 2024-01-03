from rest_framework import serializers

from .models import Players

class PlayersSerializer(serializers.ModelSerializer):
    team = serializers.CharField(source="team.team_name", read_only=True)
    class Meta:
        model = Players
        fields = (
            'player_name',
            'surname',
            'date_of_birth',
            'height',
            'weight',
            'team'
        )