from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from api.models import Beeyard, Hive, Harvest, Treatment

class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        admin = User.objects.create_user(username="Skizaru", password="pass")
        admin.is_staff = True
        admin.is_superuser = True
        admin.save()
    

