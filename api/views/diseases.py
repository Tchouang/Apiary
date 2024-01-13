from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers, viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.response import Response
from django_filters import rest_framework as filters

from api.views.serializers import DiseaseSerializer
from api.views.serializers import UserSerializer
from api.views.serializers import HiveSerializer
from api.views.serializers import BeeyardSerializer

from api.models import Hive
from api.models import Disease
from api.models import Beeyard

class DiseaseFilters(filters.FilterSet):
    class Meta:
        model = Disease
        fields = {
            'hive__registration': ['icontains', 'contains', 'exact'],
            'bool_disease' : ['exact'],
            'disease' : ['in' , 'exact'],
            'date_of_infection' : ['exact', 'gt', 'gte', 'lt', 'lte'],
            
            
        }

class DiseaseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows animals to be viewed or edited.
    """
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = DiseaseFilters
    filter_backends = [DjangoFilterBackend]