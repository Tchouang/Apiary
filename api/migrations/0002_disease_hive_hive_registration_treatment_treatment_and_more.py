# Generated by Django 5.0.1 on 2024-01-08 14:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease',
            name='hive',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='diseases', to='api.hive'),
        ),
        migrations.AddField(
            model_name='hive',
            name='registration',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='treatment',
            field=models.CharField(choices=[('OA', 'Oxalic Acid'), ('AV', 'Apivar'), ('AF', 'Antifungal')], default=None, max_length=2),
        ),
        migrations.AlterField(
            model_name='harvest',
            name='hive',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='harvests', to='api.hive'),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='hive',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='treatments', to='api.hive'),
        ),
    ]