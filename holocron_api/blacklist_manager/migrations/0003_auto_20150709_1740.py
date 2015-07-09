# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blacklist_manager', '0002_auto_20150707_2150'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entries',
            old_name='added_by',
            new_name='update_by',
        ),
        migrations.AlterField(
            model_name='entries',
            name='entry_type',
            field=models.CharField(default=b'IP', max_length=2, choices=[(b'IP', b'Single IP Address'), (b'UA', b'User Agent')]),
        ),
    ]
