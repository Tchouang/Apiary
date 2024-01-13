from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers, viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.response import Response
from django_filters import rest_framework as filters

from api.views.serializers import HarvestSerializer, TreatmentSerializer
from api.models import Harvest, Treatment

class HarvestFilters(filters.FilterSet):
    class Meta:
        model = Harvest
        fields = {
            'hive__registration': ['icontains', 'contains', 'exact'],
            'quantity': [ 'gt', 'gte', 'lt', 'lte', 'exact'],
            'harvest_date': ['exact', 'gt', 'gte', 'lt', 'lte'],
        }

class HarvestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows harvests to be viewed or edited.
    """
    queryset = Harvest.objects.all()
    serializer_class = HarvestSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = HarvestFilters
    filter_backends = [DjangoFilterBackend]
    
    
class TreatmentFilters(filters.FilterSet):
    class Meta:
        model = Treatment
        fields = { 
        "hive__registration": ['icontains', 'contains', 'exact'],
        "treatment" : ["exact"],
        "treatment_date" : ['exact', 'gt', 'gte', 'lt', 'lte'],
        }

class TreatmentViewSet(viewsets.ModelViewSet):
    
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class =TreatmentFilters
    filter_backends = [DjangoFilterBackend]