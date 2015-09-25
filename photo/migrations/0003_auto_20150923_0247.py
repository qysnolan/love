# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_auto_20150923_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
