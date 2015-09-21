# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_placement_promo_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audience_xref',
            name='a_key',
            field=models.ForeignKey(to='api.Audience', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='program',
            field=models.ForeignKey(to='api.Program', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AlterField(
            model_name='intent_xref',
            name='i_key',
            field=models.ForeignKey(to='api.Intent', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AlterField(
            model_name='lifecycle_xref',
            name='lc_key',
            field=models.ForeignKey(to='api.LifeCycle', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AlterField(
            model_name='lob_xref',
            name='lob_key',
            field=models.ForeignKey(to='api.LOB', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AlterField(
            model_name='placement',
            name='ad_network',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='api.Ad_Network', null=True),
        ),
        migrations.AlterField(
            model_name='placement',
            name='creative',
            field=models.ForeignKey(to='api.Creative', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AlterField(
            model_name='placement',
            name='medium',
            field=models.ForeignKey(to='api.Medium', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AlterField(
            model_name='placement',
            name='promo_uid',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='placement',
            name='source',
            field=models.ForeignKey(to='api.Source', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AlterField(
            model_name='placement',
            name='tactic',
            field=models.ForeignKey(to='api.Tactic', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AlterField(
            model_name='tactic',
            name='campaign',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, default=1, to='api.Campaign'),
        ),
    ]
