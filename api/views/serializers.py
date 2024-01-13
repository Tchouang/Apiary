from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Beeyard, Hive, Disease, Harvest, Treatment

class SimplifiedHiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hive
        fields = ['id', 'registration']

class BeeyardSerializer(serializers.ModelSerializer):
    hive_simplified = SimplifiedHiveSerializer(source="hives", many=True, read_only=True)
    class Meta:
        model = Beeyard
        fields= ["id", "loc_name", "user", 'hive_simplified']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class UserSerializer(serializers.ModelSerializer):
    groups_extended = GroupSerializer(source="groups", read_only=True, many=True)

    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'groups', "groups_extended"]

class HiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hive
        fields= ["id", "registration", "beeyard", "status", "date_of_status_modification", "queen_date_of_birth", "varieties"]
        
class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = ["id", "hive", "bool_disease", "disease", "date_of_infection"]
        
class HarvestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Harvest
        fields = ["id", "hive", "quantity", "harvest_date"]

class TreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treatment
        fields = ["id", "hive", "treatment", "treatment_date"]

