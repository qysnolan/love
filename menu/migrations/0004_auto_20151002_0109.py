# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_menu_isactive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='type',
            field=models.CharField(max_length=20, help_text='1-starter, 2-entree, 3-dessert'),
        ),
    ]
