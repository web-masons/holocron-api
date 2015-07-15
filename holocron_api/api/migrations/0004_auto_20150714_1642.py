# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150708_2251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad_Network',
            fields=[
                ('network_key', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('network_description', models.CharField(max_length=140)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='placement',
            name='ad_network',
            field=models.ForeignKey(blank=True, to='api.Ad_Network', null=True),
        ),
    ]
