from django.contrib.auth.models import Group
from rest_framework import serializers, viewsets, permissions
from .serializers import GroupSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]