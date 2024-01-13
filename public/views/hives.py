from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers, viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.response import Response
from django_filters import rest_framework as filters

from api.models import Hive

from api.views import HiveSerializer

class HiveFilters(filters.FilterSet):
    class Meta:
        model = Hive
        fields = {
            'registration': ['icontains', 'contains', 'exact'],
            #'beeyard': ['icontains', 'contains', 'exact'],
            'status': ['exact', 'in'],
            'date_of_status_modification' : ['exact', 'gt', 'gte', 'lt', 'lte'],
            'queen_date_of_birth' : ['exact', 'gt', 'gte', 'lt', 'lte'],
            'varieties' : ['exact', 'in']
        }
class VHiveViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows animals to be viewed
    """
    queryset = Hive.objects.all()
    serializer_class = HiveSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = HiveFilters
    filter_backends = [DjangoFilterBackend]