from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from reserva.models import Reserva, Petshop
from rest_api.serializers import AgendamentoModelSerializer, PetshopModelSerializer

class AgendamentoModelViewSet(ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = AgendamentoModelSerializer
    authentication_classes = [TokenAuthentication]
    permissions_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=False, url_path='categoria')
    def categoria(self, request):
        queryset = self.get_queryset()
        result = {}
        for choice in Reserva.TAMANHO_OPCOES:
            pets = list(queryset.filter(tamanho=choice[0]).values_list('nome_pet', flat=True))
            result[choice[1]] = {'count': len(pets), 'nome_pet': pets}
        return Response(result)

    @action(detail=False, url_path='categoria/(?P<tamanho_id>\d+)')
    def categoria_por_id(self, request, tamanho_id):
        queryset = self.get_queryset().filter(tamanho=tamanho_id)
        count = queryset.count()
        pets = list(queryset.values_list('nome_pet', flat=True))
        result = {
            'count': count,
            'tamanho': dict(Reserva.TAMANHO_OPCOES)[int(tamanho_id)],
            'nome_pet': pets,
        }
        return Response(result)

class PetshopModelViewSet(ReadOnlyModelViewSet):
    queryset = Petshop.objects.all()
    serializer_class = PetshopModelSerializer
    authentication_classes = [TokenAuthentication]
    permissions_classes = [IsAuthenticatedOrReadOnly]