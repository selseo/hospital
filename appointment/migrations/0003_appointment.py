# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ptregister', '0001_initial'),
        ('doctor_timetable', '__first__'),
        ('appointment', '0002_auto_20151005_1209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('symptom', models.CharField(max_length=100)),
                ('cause', models.CharField(max_length=100)),
                ('doctor', models.ForeignKey(to='doctor_timetable.Doctor')),
                ('patient', models.ForeignKey(to='ptregister.Patient')),
            ],
        ),
    ]
