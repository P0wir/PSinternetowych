from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views

app_name = 'bets'

bet_router = SimpleRouter()
bet_router.register('bets', views.BetViewSet, basename='bets')


odds_router = SimpleRouter()
odds_router.register('odds', views.OddsViewSet, basename='odds')

urlpatterns = [
    path('', include(bet_router.urls)),
    path('', include(odds_router.urls)),
]