import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Teams
from .serializers import TeamsSerializer


class TeamsFilter:
    pass


class TeamsViewSet(viewsets.ModelViewSet):
    serializer_class = TeamsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Teams.objects.all()
    search_fields = ['team_name', 'year', 'city', 'conference']
    ordering_fields = ['year']
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, SearchFilter, OrderingFilter)
