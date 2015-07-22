# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_tactic_campaign'),
    ]

    operations = [
        migrations.RenameField(
            model_name='placement',
            old_name='pageCat',
            new_name='page_cat',
        ),
        migrations.RenameField(
            model_name='placement',
            old_name='pageID',
            new_name='page_id',
        ),
    ]
