# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menu_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True)),
                ('recip', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, upload_to='menu')),
                ('last_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['menu_id'],
            },
        ),
    ]
