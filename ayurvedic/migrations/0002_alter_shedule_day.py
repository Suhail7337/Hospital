# Generated by Django 5.0.1 on 2024-02-04 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ayurvedic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shedule',
            name='day',
            field=models.DateField(blank=True, null=True),
        ),
    ]
