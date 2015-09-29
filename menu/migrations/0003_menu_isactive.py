# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20150925_0232'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
    ]
