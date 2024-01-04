from rest_framework import serializers

from .models import Players

class PlayersSerializer(serializers.ModelSerializer):
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