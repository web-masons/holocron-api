# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlacklistEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entry_type', models.CharField(default=b'IP', max_length=2, choices=[(b'IP', b'Single IP Address'), (b'UA', b'User Agent'), (b'IR', b'Range of IP Addresses')])),
                ('description', models.CharField(max_length=100)),
                ('added_by', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('entry', models.CharField(max_length=100)),
            ],
        ),
    ]
