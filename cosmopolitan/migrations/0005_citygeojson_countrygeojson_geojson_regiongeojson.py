# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosmopolitan', '0004_postcode_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeoJSON',
            fields=[
                ('id', models.CharField(max_length=400, primary_key=True, serialize=False)),
                ('geojson', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CityGeoJSON',
            fields=[
                ('geojson_ptr', models.OneToOneField(parent_link=True, serialize=False, to='cosmopolitan.GeoJSON', primary_key=True, auto_created=True)),
                ('city', models.OneToOneField(to='cosmopolitan.City')),
            ],
            bases=('cosmopolitan.geojson',),
        ),
        migrations.CreateModel(
            name='CountryGeoJSON',
            fields=[
                ('geojson_ptr', models.OneToOneField(parent_link=True, serialize=False, to='cosmopolitan.GeoJSON', primary_key=True, auto_created=True)),
                ('country', models.OneToOneField(to='cosmopolitan.Country')),
            ],
            bases=('cosmopolitan.geojson',),
        ),
        migrations.CreateModel(
            name='RegionGeoJSON',
            fields=[
                ('geojson_ptr', models.OneToOneField(parent_link=True, serialize=False, to='cosmopolitan.GeoJSON', primary_key=True, auto_created=True)),
                ('region', models.OneToOneField(to='cosmopolitan.Region')),
            ],
            bases=('cosmopolitan.geojson',),
        ),
    ]
