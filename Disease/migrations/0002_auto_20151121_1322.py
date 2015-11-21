# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Disease', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disease',
            name='availability',
            field=models.BooleanField(default=True),
        ),
    ]
