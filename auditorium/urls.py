from django.urls import path, include
from .api import views
from rest_framework import routers
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings


router = routers.DefaultRouter()
router.register('reservation', views.AuditoriumReservationView)

urlpatterns = [
    path('', include(router.urls)),
]