# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('person_name', models.CharField(max_length=255, default='Anonymous')),
                ('comment', models.TextField(blank=True)),
                ('isActive', models.BooleanField(default=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['last_update'],
            },
        ),
    ]
