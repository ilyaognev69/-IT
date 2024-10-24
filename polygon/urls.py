from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import PolygonViewSet

router = DefaultRouter()
router.register(r'polygons', PolygonViewSet)

urlpatterns = [
    path('', views.polygon_view, name='polygon_view'),
	path('api/', include(router.urls))
]
