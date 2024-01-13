from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers, viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.response import Response
from django_filters import rest_framework as filters

from api.views.serializers import BeeyardSerializer
from api.models import Beeyard, Hive, Treatment

class BeeyardFilters(filters.FilterSet):
    class Meta:
        model = Beeyard
        fields = {
            'loc_name': ['icontains', 'contains', 'exact'],
            'user__first_name': ['icontains', 'contains', 'exact'],
            'user__last_name': ['icontains', 'contains', 'exact'],
        }

class VBeeyardViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows animals to be viewed
    """
    queryset = Beeyard.objects.all()
    serializer_class = BeeyardSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = BeeyardFilters
    filter_backends = [DjangoFilterBackend]