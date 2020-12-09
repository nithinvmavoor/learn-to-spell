from django.urls import path
from .views import HomePageView
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'api/animals', views.AnimalsViewSet)
router.register(r'api/colours', views.ColoursViewSet)
router.register(r'api/fruits', views.FruitsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]