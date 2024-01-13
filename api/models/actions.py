from django.db import models

#héritage non fait par peur des conséquences de l'héritage en diamant
class Harvest(models.Model):
    hive = models.ForeignKey('Hive', on_delete=models.CASCADE, related_name='harvests', null=True, blank=True, default=None)
    quantity = models.FloatField()
    harvest_date = models.DateField()
    
class Treatment(models.Model):
    hive = models.ForeignKey('Hive', on_delete=models.CASCADE, related_name='treatments', null=True, blank=True, default=None)
    TREATMENT_CHOICES=[
        ("OA","Oxalic Acid"),
        ("AV","Apivar"),
        ("AF","Antifungal")
    ]
    treatment = models.CharField(max_length=2, choices=TREATMENT_CHOICES,default=None)
    treatment_date = models.DateField()
    
    