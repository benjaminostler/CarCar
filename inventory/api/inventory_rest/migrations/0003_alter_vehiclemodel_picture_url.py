# Generated by Django 4.0.3 on 2024-04-18 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_rest', '0002_automobile_sold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiclemodel',
            name='picture_url',
            field=models.URLField(max_length=500),
        ),
    ]
