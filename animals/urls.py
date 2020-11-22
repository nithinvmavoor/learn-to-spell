from django.urls import path
from .views import HomePageView
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'animals', views.AnimalsViewSet)
router.register(r'colours', views.ColoursViewSet)
router.register(r'fruits', views.FruitsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]