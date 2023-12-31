from rest_framework import serializers
from .models import Teams

class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = (
            'team_name',
            'year',
            'city',
            'conference'
        )