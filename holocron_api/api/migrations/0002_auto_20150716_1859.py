# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from api.models import Program, Campaign

def initial_program(apps, schema_editor):
    first_program = Program.objects.create(program_name = "General Business",
                                           program_description = "Default collection of general business campaigns",
                                           created_by = "system")


def initial_campaign(apps, schema_editor):
    first_campaign = Campaign.objects.create(campaign_name = 'No Attribution',
                                             campaign_description = 'Tactics with no known campaign attribution.  If not empty, please attribute correctly.',
                                             created_by = 'system',
                                             program=Program.objects.get(program_id=1))

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_squashed_0005_auto_20150716_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('campaign_id', models.AutoField(serialize=False, primary_key=True)),
                ('campaign_name', models.CharField(max_length=100)),
                ('campaign_description', models.CharField(max_length=140)),
                ('created_by', models.CharField(max_length=100)),
                ('campaign_notes', models.CharField(max_length=140, blank=True)),
                ('start_date', models.DateField(null=True, verbose_name=b'Start Date', blank=True)),
                ('end_date', models.DateField(null=True, verbose_name=b'End Date', blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('program_id', models.AutoField(serialize=False, primary_key=True)),
                ('program_name', models.CharField(max_length=100)),
                ('program_description', models.CharField(max_length=140)),
                ('created_by', models.CharField(max_length=100)),
                ('program_notes', models.CharField(max_length=140, blank=True)),
                ('start_date', models.DateField(null=True, verbose_name=b'Start Date', blank=True)),
                ('end_date', models.DateField(null=True, verbose_name=b'End Date', blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='campaign',
            name='program',
            field=models.ForeignKey(to='api.Program'),
        ),
        migrations.RunPython(initial_program),
        migrations.RunPython(initial_campaign)
    ]
