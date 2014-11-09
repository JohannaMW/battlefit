# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fithack', '0002_auto_20141109_0252'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='category',
            field=models.CharField(default=b'W', max_length=1, choices=[(b'W', b'Weight Loss'), (b'H', b'Health'), (b'F', b'Fitness')]),
            preserve_default=True,
        ),
    ]
