from rest_framework.routers import SimpleRouter

from . import views

app_name = 'players'

router = SimpleRouter()

router.register('', views.PlayersViewSet, basename='Players')

urlpatterns = router.urls