from rest_framework.routers import SimpleRouter

from . import views

app_name = 'teams'

router = SimpleRouter()

router.register('', views.TeamsViewSet, basename='Teams')

urlpatterns = router.urls