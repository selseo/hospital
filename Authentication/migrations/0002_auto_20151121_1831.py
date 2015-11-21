# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='idcard',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='userprofile',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='idcard',
            field=models.CharField(max_length=20, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(max_length=15, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(max_length=1, default=0),
            preserve_default=False,
        ),
    ]
