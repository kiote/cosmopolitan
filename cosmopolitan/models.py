from django.contrib.gis.db import models


class Continent(models.Model):
    id = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=50, blank=False)
    geoNameId = models.PositiveIntegerField(blank=False)
    countries = models.ManyToManyField("cosmopolitan.Country", related_name="related_continent_country")
    currencies = models.ManyToManyField("cosmopolitan.Currency")


class Country(models.Model):
    id = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=200, db_index=True, verbose_name="ascii name")
    slug = models.CharField(max_length=200)
    population = models.IntegerField()
    code3 = models.CharField(max_length=3)
    currency = models.ForeignKey("cosmopolitan.Currency", null=True)
    continent = models.ForeignKey("cosmopolitan.Continent", null=True)
    polygon = models.TextField(null=True)


class Currency(models.Model):
    id = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=50, null=False)
    countries = models.ManyToManyField("cosmopolitan.Country", related_name="related_country")
    continents = models.ManyToManyField("cosmopolitan.Continent")


class Region(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200, db_index=True, verbose_name="ascii name")
    name_std = models.CharField(max_length=200, db_index=True, verbose_name="standard name")
    country = models.ForeignKey("cosmopolitan.Country")
    polygon = models.TextField(null=True)


class City(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200, db_index=True, verbose_name="ascii name")
    name_std = models.CharField(max_length=200, db_index=True, verbose_name="standard name")
    location = models.PointField()
    population = models.IntegerField()
    region = models.ForeignKey("cosmopolitan.Region", null=True, blank=True)
    country = models.ForeignKey("cosmopolitan.Country")
    elevation = models.IntegerField(null=True)
    kind = models.CharField(max_length=10) # http://www.geonames.org/export/codes.html
    timezone = models.CharField(max_length=40)
    polygon = models.TextField(null=True)


class Postcode(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    location = models.PointField()

    country = models.ForeignKey(Country, related_name = 'postal_codes')

    # Region names for each admin level, region may not exist in DB
    region_name = models.CharField(max_length=100, db_index=True)
    subregion_name = models.CharField(max_length=100, db_index=True)
    district_name = models.CharField(max_length=100, db_index=True)

    region = models.ForeignKey("cosmopolitan.Region", null=True, blank=True)
