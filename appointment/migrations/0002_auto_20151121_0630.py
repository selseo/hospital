# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='patient',
            new_name='patient_id',
        ),
        migrations.RenameField(
            model_name='timetable',
            old_name='time2',
            new_name='afternoon',
        ),
        migrations.RenameField(
            model_name='timetable',
            old_name='dr',
            new_name='doctor_id',
        ),
        migrations.RenameField(
            model_name='timetable',
            old_name='time1',
            new_name='morning',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='doctor',
        ),
        migrations.AddField(
            model_name='appointment',
            name='timetable_id',
            field=models.ForeignKey(default=1, to='appointment.timeTable'),
            preserve_default=False,
        ),
    ]
