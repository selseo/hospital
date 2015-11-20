# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '__first__'),
        ('Medicine', '0001_initial'),
        ('Disease', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientVisitInfo',
            fields=[
                ('appointment', models.OneToOneField(serialize=False, to='appointment.Appointment', primary_key=True)),
                ('weight', models.DecimalField(null=True, max_digits=4, decimal_places=1, validators=['weightTooMuch'])),
                ('height', models.DecimalField(null=True, max_digits=4, decimal_places=1)),
                ('pulse', models.IntegerField(null=True)),
                ('systolic', models.IntegerField(null=True)),
                ('diastolic', models.IntegerField(null=True)),
                ('status', models.IntegerField()),
                ('lastUpdate', models.DateTimeField(auto_now=True)),
                ('note', models.CharField(null=True, max_length=200)),
                ('diseases', models.ManyToManyField(to='Disease.Disease')),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('amount', models.IntegerField()),
                ('usage', models.CharField(max_length=200)),
                ('medicines', models.ForeignKey(to='Medicine.Medicine')),
                ('patientVisitInfo', models.ForeignKey(to='Visit.PatientVisitInfo')),
            ],
        ),
        migrations.AddField(
            model_name='patientvisitinfo',
            name='medicines',
            field=models.ManyToManyField(to='Medicine.Medicine', through='Visit.Prescription'),
        ),
    ]
