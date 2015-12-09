# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

from cities.models import Country

from currencies.models import Currency
from continents.models import Continent

def seed_data(apps, schema_editor):
    ExtraCountry = apps.get_model("extra_countries", "ExtraCountry")
    for country in Country.objects.all():
        print("seeding data for county: %s" % country.name)
        currency = Currency.objects.get(name=country.currency_name.strip(), code=country.currency)
        continent = Continent.objects.get(code=country.continent)
        ex = ExtraCountry(extra_currency_id=currency.pk, extra_continent_id=continent.pk, country_id=country.pk)
        ex.save()

def reverse_data(apps, schema_editor):
    ExtraCountry = apps.get_model("extra_countries", "ExtraCountry")
    ExtraCountry.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('extra_countries', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_data, reverse_data)
    ]
