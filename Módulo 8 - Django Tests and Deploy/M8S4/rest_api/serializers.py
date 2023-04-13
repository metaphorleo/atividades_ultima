import datetime
from rest_framework.serializers import (
    ModelSerializer, 
    HyperlinkedRelatedField, 
    PrimaryKeyRelatedField, 
    ValidationError
)
from reserva.models import Petshop, Reserva

class PetshopModelSerializer(ModelSerializer):
    reservas = HyperlinkedRelatedField(
        many = True,
        read_only = True,
        view_name = 'api:reserva-detail'
    )

    class Meta:
        model = Petshop
        fields = '__all__'

class PetshopNestedModelSerializer(ModelSerializer):
    class Meta:
        model = Petshop
        fields = '__all__'

class PetshopRelatedFieldCustomSerializer(PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        self.serializer = PetshopNestedModelSerializer
        super().__init__(**kwargs)

    def use_pk_only_optimization(self):
        return False
    
    def to_representation(self, value):
        return self.serializer(value, context = self.context).data

class AgendamentoModelSerializer(ModelSerializer):
    petshop = PetshopRelatedFieldCustomSerializer(
        queryset = Petshop.objects.all(),
        read_only = False
    )
    
    def validate_dia_reserva(self, value):
        hoje = datetime.date.today()
        if value < hoje:
            raise ValidationError('Data inválida, não é possível realizar uma reserva para o passado.')
        return value

    class Meta:
        model = Reserva
        fields = '__all__'