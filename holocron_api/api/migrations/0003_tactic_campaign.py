# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150716_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='tactic',
            name='campaign',
            field=models.ForeignKey(default=1, to='api.Campaign'),
        ),
    ]
