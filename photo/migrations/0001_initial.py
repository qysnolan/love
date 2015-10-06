# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('photo_id', models.IntegerField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('path', models.ImageField(upload_to='photos')),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'ordering': ['title', 'photo_id'],
            },
        ),
    ]
