from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_api.views import AgendamentoModelViewSet

app_name = 'rest_api'

router = DefaultRouter(trailing_slash=False)
router.register('agendamento', AgendamentoModelViewSet)

urlpatterns = []

urlpatterns += router.urls