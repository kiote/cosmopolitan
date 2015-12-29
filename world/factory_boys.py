import factory
from factory.fuzzy import FuzzyText

from django.contrib.gis.geos import GEOSGeometry

from continents.models import Continent
from currencies.models import Currency
from extra_countries.models import ExtraCountry

from cities.models import Country
from cities.models import Region
from cities.models import City


class CountryFactory(factory.DjangoModelFactory):
    class Meta:
        model = Country

    name = FuzzyText(length=6)
    population = 1


class RegionFactory(factory.DjangoModelFactory):
    class Meta:
        model = Region

    name = FuzzyText(length=6)
    country = factory.SubFactory(CountryFactory)


class CityFactory(factory.DjangoModelFactory):
    class Meta:
        model = City

    name = FuzzyText(length=6)
    location = GEOSGeometry('POINT(5 23)')
    population = 1
    country = factory.SubFactory(CountryFactory)
    region = factory.SubFactory(RegionFactory)


class ContinentFactory(factory.DjangoModelFactory):
    class Meta:
        model = Continent

    code = FuzzyText(length=2)
    name = FuzzyText(length=6)
    geoNameId = 12


class CurrencyFactory(factory.DjangoModelFactory):
    class Meta:
        model = Currency

    code = FuzzyText(length=2)
    name = FuzzyText(length=6)


class ExtraCountryFactory(factory.DjangoModelFactory):
    class Meta:
        model = ExtraCountry

    code = FuzzyText(length=2)
    country = factory.SubFactory(CountryFactory)
    extra_continent = factory.SubFactory(ContinentFactory)
    extra_currency = factory.SubFactory(CurrencyFactory)
