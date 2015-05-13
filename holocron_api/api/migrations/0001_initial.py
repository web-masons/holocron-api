# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('campaign_id', models.AutoField(serialize=False, primary_key=True)),
                ('campaign_name', models.CharField(max_length=100)),
                ('campaign_description', models.CharField(max_length=140)),
                ('end_date', models.DateField(verbose_name=b'End Date')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('content_id', models.AutoField(serialize=False, primary_key=True)),
                ('content_name', models.CharField(max_length=100)),
                ('content_description', models.CharField(max_length=140)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medium',
            fields=[
                ('medium_id', models.AutoField(serialize=False, primary_key=True)),
                ('medium_name', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Placement',
            fields=[
                ('placement_id', models.AutoField(serialize=False, primary_key=True)),
                ('placement_name', models.CharField(max_length=100)),
                ('placement_url', models.CharField(max_length=100)),
                ('end_date', models.DateField(verbose_name=b'End Date')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('campaign', models.ForeignKey(to='api.Campaign')),
                ('content', models.ForeignKey(to='api.Content')),
                ('medium', models.ForeignKey(to='api.Medium')),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('source_id', models.AutoField(serialize=False, primary_key=True)),
                ('source_name', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='placement',
            name='source',
            field=models.ForeignKey(to='api.Source'),
        ),
    ]
