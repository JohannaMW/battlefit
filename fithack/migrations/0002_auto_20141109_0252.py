# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fithack', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='goal',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='age',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='gender',
            field=models.CharField(default=b'F', max_length=1, choices=[(b'F', b'Female'), (b'M', b'Male')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='height',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='weight',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='pic',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='score',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
