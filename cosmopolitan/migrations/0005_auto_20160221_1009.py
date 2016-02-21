# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosmopolitan', '0004_postcode_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='polygon',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='polygon',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='region',
            name='polygon',
            field=models.TextField(null=True),
        ),
    ]
