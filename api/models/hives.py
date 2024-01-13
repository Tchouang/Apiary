from django.db import models

class Hive(models.Model):
    registration = models.CharField(max_length=50, null=True, blank=True)
    beeyard = models.ForeignKey('Beeyard', on_delete=models.CASCADE, related_name='hives')
    STATUS_CHOICES = [
        ("Active", "Active"),
        ("Waiting", "Waiting"),
        ("Destroyed", "Destroyed"),
    ]
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    date_of_status_modification = models.DateField()
    #automatisation possible
    
    queen_date_of_birth=models.DateField()
    
    BEE_VARIETIES_CHOICES = [
        ("Buckfast", "Buckfast"),
        ("Apis mellifera mellifera", "Apis mellifera mellifera "),
        ("Apis mellifera ligustica", "Apis mellifera ligustica"),
    ]
    varieties = models.CharField(max_length=50, choices=BEE_VARIETIES_CHOICES)
    
    def __str__(self):
        status_label = dict(self.STATUS_CHOICES).get(self.status, '')
        bee_variety_label =dict(self.BEE_VARIETIES_CHOICES).get(self.status, '')
        return f"{self.registration} - {status_label} - {bee_variety_label}"
    
    
    