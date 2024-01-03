from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

app_name = 'matches'

router = SimpleRouter()

router.register('', views.MatchesViewSet, basename='Matches')

urlpatterns = router.urls