# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0004_auto_20150923_0313'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
    ]
