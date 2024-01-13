from django.db import models
from django.contrib.auth.models import User

class Beeyard(models.Model):
    loc_name = models.CharField(max_length=100)#name of the place of the beeyard
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='beeyards')
    #User doit être sans quote
    #faire le lien vers user au lieu de beekeeper
    def __str__(self):
        return f"{self.loc_name} - {self.user}"