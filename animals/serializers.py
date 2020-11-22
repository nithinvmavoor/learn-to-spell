from rest_framework import serializers

from .models import Animals
from .models import Fruits
from .models import Colours

class AnimalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Animals
        fields = ('name', 'image', 'id')
class FruitSerial(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fruits
        fields = ('name', 'image', 'id')
class ColourSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Colours
        fields = ('name', 'image', 'id')