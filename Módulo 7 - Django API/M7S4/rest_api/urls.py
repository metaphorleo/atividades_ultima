from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_api.views import AgendamentoModelViewSet, PetshopModelViewSet

app_name = 'rest_api'

router = DefaultRouter(trailing_slash=False)
router.register('agendamento', AgendamentoModelViewSet)
router.register('petshop', PetshopModelViewSet)

urlpatterns = []

urlpatterns += router.urls