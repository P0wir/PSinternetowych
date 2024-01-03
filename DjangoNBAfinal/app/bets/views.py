import django_filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Bet,Odds
from .serializers import BetSerializer,OddsSerializer

class BetViewSet(viewsets.ModelViewSet):
    serializer_class = BetSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Bet.objects.all()
    search_fields = ['match__team_home__team_name', 'match__team_away__team_name', 'id', 'selected_team', 'user']
    ordering_fields = ['id','selected_team','user','money']
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, SearchFilter, OrderingFilter)


class OddsViewSet(viewsets.ModelViewSet):
    serializer_class = OddsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Odds.objects.all()
    search_fields = ['match__team_home__team_name', 'match__team_away__team_name', 'id', 'team', 'odds_value']
    ordering_fields = ['id','selected_team','user']
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, SearchFilter, OrderingFilter)

