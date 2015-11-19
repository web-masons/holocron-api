# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20150921_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='placement',
            name='placement_description',
            field=models.CharField(max_length=140, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='campaign_name',
            field=models.CharField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='medium',
            name='medium_name',
            field=models.CharField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='placement',
            name='creative',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='api.Creative', null=True),
        ),
        migrations.AlterField(
            model_name='placement',
            name='placement_name',
            field=models.CharField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='program',
            name='program_name',
            field=models.CharField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='source',
            name='source_name',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
