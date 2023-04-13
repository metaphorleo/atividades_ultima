from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_api.views import AgendamentoModelViewSet, PetshopModelViewSet

app_name = 'rest_api'

router = DefaultRouter(trailing_slash=False)
router.register('agendamento', AgendamentoModelViewSet)
router.register('petshop', PetshopModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('categoria/', AgendamentoModelViewSet.as_view({'get': 'categoria'}), name='categoria'),
    path('categoria/<int:tamanho_id>/', AgendamentoModelViewSet.as_view({'get': 'categoria_por_id'}), name='categoria-por-id'),
]

urlpatterns += router.urls