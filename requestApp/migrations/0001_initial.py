# Generated by Django 3.2 on 2023-06-13 07:13

from django.conf import settings
import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Req_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('req_order_slug', models.SlugField(blank=True, null=True)),
                ('req_order_title', models.CharField(max_length=250)),
                ('purpose', models.CharField(blank=True, max_length=20, null=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(15.3725629, 44.2396769), srid=4326)),
                ('property_town', models.CharField(default="sana'a", max_length=50)),
                ('rent_frequency', models.CharField(default='monthly', max_length=50)),
                ('ownership_type', models.CharField(blank=True, max_length=20, null=True)),
                ('property_description', models.TextField(blank=True, null=True)),
                ('property_price', models.IntegerField(blank=True, null=True)),
                ('phone', models.CharField(default='776278868', max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('rooms', models.CharField(default='2', max_length=50)),
                ('baths', models.CharField(default='2', max_length=10)),
                ('furnishingStatus', models.BooleanField(default=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Request_order',
                'verbose_name_plural': 'Request_order',
            },
        ),
    ]
