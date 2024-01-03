import django_filters
from teams.models import Teams
from .models import Players

class PlayersFilter(django_filters.FilterSet):
    team = django_filters.ModelMultipleChoiceFilter(to_field_name='id', queryset=Teams.objects.all())

    class Meta:
        model = Players
        fields = ['team']