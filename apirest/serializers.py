
from rest_framework import serializers 
from apirest.models import Sensores
 
 
class SensoresSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Sensores
        fields = ('id',
                 'temperatura',
                 'humedad',
                 'peso')

