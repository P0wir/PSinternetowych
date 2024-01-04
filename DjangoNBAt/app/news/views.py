import django_filters
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from app.permissions import ReadOnlyOrAdminOnly

from .models import News
from .serializers import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (ReadOnlyOrAdminOnly,)
    queryset = News.objects.all()
    search_fields = ['title', 'content', 'author__username', 'publication_date']
    ordering_fields = ['publication_date']
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, SearchFilter, OrderingFilter)
