import django_filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from .models import Schedule
from .serializers import ScheduleSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    serializer_class = ScheduleSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Schedule.objects.all()
    search_fields = ['team_home__team_name', 'team_away__team_name', 'date', 'location']
    ordering_fields = ['team_home', 'team_away', 'date']
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, SearchFilter, OrderingFilter)
