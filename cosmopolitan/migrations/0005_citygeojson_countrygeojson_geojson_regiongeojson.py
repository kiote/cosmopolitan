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
                ('id', models.CharField(serialize=False, max_length=400, primary_key=True)),
                ('geojson', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CityGeoJSON',
            fields=[
                ('geojson_ptr', models.OneToOneField(auto_created=True, to='cosmopolitan.GeoJSON', primary_key=True, parent_link=True, serialize=False)),
                ('city', models.ForeignKey(to='cosmopolitan.City')),
            ],
            bases=('cosmopolitan.geojson',),
        ),
        migrations.CreateModel(
            name='CountryGeoJSON',
            fields=[
                ('geojson_ptr', models.OneToOneField(auto_created=True, to='cosmopolitan.GeoJSON', primary_key=True, parent_link=True, serialize=False)),
                ('country', models.ForeignKey(to='cosmopolitan.Country')),
            ],
            bases=('cosmopolitan.geojson',),
        ),
        migrations.CreateModel(
            name='RegionGeoJSON',
            fields=[
                ('geojson_ptr', models.OneToOneField(auto_created=True, to='cosmopolitan.GeoJSON', primary_key=True, parent_link=True, serialize=False)),
                ('region', models.ForeignKey(to='cosmopolitan.Region')),
            ],
            bases=('cosmopolitan.geojson',),
        ),
    ]
