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
    filter_backends = [DjangoFilterBackend]
    
    @action(
        detail=True,
        methods=["PATCH"]
    )
    def treatment_par(self, request, pk):
        current_beeyard = Beeyard.objects.filter(pk=pk).first()
        treatment = request.data.get("treatment")
        treatment_date = request.data.get("treatment_date")
        hives = Hive.objects.filter(beeyard=current_beeyard)
        if current_beeyard is not None:
            for hive in hives:
                Treatment.objects.filter(hive=hive).update_or_create(hive=hive, treatment=treatment, treatment_date=treatment_date)
            return Response(status=status.HTTP_200_OK) 
        return Response(status=status.HTTP_400_BAD_REQUEST)
#to be pasted in postman PATCH to treat the beeyard 1 with ApiVar the 2023-01-01:
# http://127.0.0.1:8000/beeyard/1/treatment_par/
# json : 
# {
# "treatment":"AV",
# "treatment_date":"2023-01-01"
# }
