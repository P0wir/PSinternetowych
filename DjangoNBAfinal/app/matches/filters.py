import django_filters
from teams.models import Teams
from .models import Matches

class PlayersFilter(django_filters.FilterSet):
    team = django_filters.ModelMultipleChoiceFilter(to_field_name='id', queryset=Teams.objects.all())

    class Meta:
        model = Matches
        fields = ['team_home', 'team_away']