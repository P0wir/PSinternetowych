import django_filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from app.permissions import ReadOnlyOrAdminOnly

from .models import Matches
from .serializers import MatchesSerializer

class MatchesViewSet(viewsets.ModelViewSet):
    serializer_class = MatchesSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (ReadOnlyOrAdminOnly,)
    queryset = Matches.objects.all()
    search_fields = ['team_home__team_name', 'team_away__team_name', 'date', 'location']
    ordering_fields = ['team_home', 'team_away', 'date', 'score_home','score_away']
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, SearchFilter, OrderingFilter)

