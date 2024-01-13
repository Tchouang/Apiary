from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from api.views import UserSerializer

class VUserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]