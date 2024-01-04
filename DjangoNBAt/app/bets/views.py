import django_filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from app.permissions import ReadOnlyOrAdminOnly, CreateOrAdminOnly, ReadOnlyOrStaff

from .models import Bet,Odds
from .serializers import BetSerializer,OddsSerializer

class BetViewSet(viewsets.ModelViewSet):
    serializer_class = BetSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (CreateOrAdminOnly,)
    queryset = Bet.objects.all()
    search_fields = ['id', 'selected_team__team_name', 'user__id']
    ordering_fields = ['id','selected_team__team_name','money', 'user__id']
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, SearchFilter, OrderingFilter)


class OddsViewSet(viewsets.ModelViewSet):
    serializer_class = OddsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (ReadOnlyOrStaff,)
    queryset = Odds.objects.all()
    search_fields = ['match__team_home__team_name', 'match__team_away__team_name', 'id', 'team__team_name', 'odds_value']
    ordering_fields = ['id','selected_team']
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, SearchFilter, OrderingFilter)

