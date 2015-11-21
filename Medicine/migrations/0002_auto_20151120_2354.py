# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medicine', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicine',
            name='id',
        ),
        migrations.AlterField(
            model_name='medicine',
            name='name',
            field=models.CharField(max_length=300, primary_key=True, serialize=False),
        ),
    ]
