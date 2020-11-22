from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from django.views.generic import ListView
from .models import Animals
from .models import Fruits
from .models import Colours

from .serializers import AnimalSerializer
from .serializers import ColourSerializer
from .serializers import FruitSerial


class HomePageView(ListView):
    model = Animals
    #template_name = 'home.html'

class AnimalsViewSet(viewsets.ModelViewSet):
    queryset = Animals.objects.all().order_by('name')
    serializer_class = AnimalSerializer

class FruitsViewSet(viewsets.ModelViewSet):
    queryset = Fruits.objects.all().order_by('name')
    serializer_class = FruitSerial

class ColoursViewSet(viewsets.ModelViewSet):
    queryset = Colours.objects.all().order_by('name')
    serializer_class = ColourSerializer