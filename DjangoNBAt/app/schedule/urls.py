from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

app_name = 'schedule'

router = SimpleRouter()

router.register('', views.ScheduleViewSet, basename='Schedule')

urlpatterns = router.urls