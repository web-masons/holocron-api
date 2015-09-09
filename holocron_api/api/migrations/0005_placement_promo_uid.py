# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20150721_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='placement',
            name='promo_uid',
            field=models.IntegerField(max_length=5, null=True, blank=True),
        ),
    ]
