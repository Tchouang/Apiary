from django.contrib import admin
from .models import Beeyard, Hive, Disease, Harvest, Treatment
# Register your models here.

class BeeyardAdmin(admin.ModelAdmin):
    list_display = ('loc_name', 'user')
    list_filter = ('loc_name','user')
    search_fields = ('loc_name', 'user')

class HiveAdmin(admin.ModelAdmin):
    list_display = ('registration','beeyard','status', 'date_of_status_modification', 'queen_date_of_birth', 'varieties')
    list_filter =('registration','beeyard','status', 'date_of_status_modification', 'queen_date_of_birth', 'varieties')
    search_fields =('registration' ,'beeyard','status', 'date_of_status_modification', 'queen_date_of_birth', 'varieties')

class DiseaseAdmin(admin.ModelAdmin):
    list_display = ('hive','bool_disease','disease','date_of_infection')
    list_filter =('hive','bool_disease','disease','date_of_infection')
    search_fields =('hive','bool_disease','disease','date_of_infection')

class HarvestAdmin(admin.ModelAdmin):
    list_display = ('hive','quantity','harvest_date')
    list_filter =('hive','quantity','harvest_date')
    search_fields =('hive','quantity','harvest_date')

class TreatmentAdmin(admin.ModelAdmin):
    list_display = ('hive','treatment','treatment_date')
    list_filter =('hive','treatment','treatment_date')
    search_fields =('hive','treatment','treatment_date')

# Enregistrement des modèles avec leurs configurations d'administration personnalisées
admin.site.register(Beeyard, BeeyardAdmin)
admin.site.register(Hive, HiveAdmin)
admin.site.register(Harvest, HarvestAdmin)
admin.site.register(Treatment, TreatmentAdmin)
admin.site.register(Disease, DiseaseAdmin)