# Generated by Django 4.1 on 2023-05-21 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appRealestate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='furnishingStatus',
            field=models.BooleanField(default=True),
        ),
    ]