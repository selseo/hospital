# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('ICD10', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('SNOMED', models.CharField(null=True, max_length=20)),
                ('DRG', models.CharField(null=True, max_length=20)),
                ('name', models.CharField(null=True, max_length=20)),
                ('availability', models.BooleanField()),
            ],
        ),
    ]
