# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audience',
            fields=[
                ('audience_key', models.SlugField(serialize=False, primary_key=True)),
                ('audience_description', models.CharField(max_length=140)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('campaign_key', models.SlugField(max_length=100, serialize=False, primary_key=True)),
                ('campaign_name', models.CharField(max_length=100)),
                ('campaign_description', models.CharField(max_length=140)),
                ('created_by', models.CharField(max_length=100)),
                ('campaign_notes', models.CharField(max_length=140, blank=True)),
                ('end_date', models.DateField(verbose_name=b'End Date')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Creative',
            fields=[
                ('creative_id', models.AutoField(serialize=False, primary_key=True)),
                ('creative_name', models.CharField(max_length=100)),
                ('creative_description', models.CharField(max_length=140)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Intent',
            fields=[
                ('intent_key', models.SlugField(serialize=False, primary_key=True)),
                ('intent_description', models.CharField(max_length=140)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='LifeCycle',
            fields=[
                ('lifecycle_key', models.SlugField(serialize=False, primary_key=True)),
                ('lifecycle_description', models.CharField(max_length=140)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='LOB',
            fields=[
                ('lob_key', models.SlugField(serialize=False, primary_key=True)),
                ('lob_description', models.CharField(max_length=140)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medium',
            fields=[
                ('medium_key', models.SlugField(max_length=100, serialize=False, primary_key=True)),
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
                ('catid', models.IntegerField(null=True, blank=True)),
                ('jira_ticket', models.CharField(default=b'', max_length=20, blank=True)),
                ('end_date', models.DateField(verbose_name=b'End Date')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('campaign', models.ForeignKey(to='api.Campaign')),
                ('creative', models.ForeignKey(to='api.Creative')),
                ('medium', models.ForeignKey(to='api.Medium')),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('source_key', models.SlugField(max_length=100, serialize=False, primary_key=True)),
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
        migrations.AddField(
            model_name='lob',
            name='placements',
            field=models.ManyToManyField(to='api.Placement'),
        ),
        migrations.AddField(
            model_name='lifecycle',
            name='placements',
            field=models.ManyToManyField(to='api.Placement'),
        ),
        migrations.AddField(
            model_name='intent',
            name='placements',
            field=models.ManyToManyField(to='api.Placement'),
        ),
        migrations.AddField(
            model_name='audience',
            name='placements',
            field=models.ManyToManyField(to='api.Placement'),
        ),
    ]
