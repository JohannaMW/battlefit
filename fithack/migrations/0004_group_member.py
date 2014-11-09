# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('fithack', '0003_group_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='member',
            field=models.ManyToManyField(related_name='member', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
