from django.db import models
    #si oui je peux le traiter dans Django
    #pouvoir dater les infections et avoir un historique
    
class Disease(models.Model):
    hive = models.ForeignKey('Hive', on_delete=models.CASCADE, related_name='diseases',null=True, blank=True)
    bool_disease = models.BooleanField(default=False)
    
    DISEASES_CHOICES = [
        ("Varroa mite", "Varroa mite"),
        ("Acarapis woodi","Acarapis woodi"),
    ]
    disease = models.CharField(max_length=15, choices=DISEASES_CHOICES)
    date_of_infection = models.DateField()
    
    def __str__(self):
        disease_label = dict(self.DISEASES_CHOICES).get(self.disease, '')
        return f"{self.hive} - {self.bool_disease} - {self.date_of_infection} - {disease_label}"