import django_filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from app.permissions import ReadOnlyOrAdminOnly

from .models import Players
from .serializers import PlayersSerializer

class PlayersViewSet(viewsets.ModelViewSet):
    serializer_class = PlayersSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (ReadOnlyOrAdminOnly,)
    queryset = Players.objects.all()
    search_fields = ['player_name', 'surname', 'team__team_name']
    ordering_fields = ['player_name', 'surname', 'weight', 'height']
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, SearchFilter, OrderingFilter)

