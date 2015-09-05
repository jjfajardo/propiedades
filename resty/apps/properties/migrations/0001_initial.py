# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import resty.apps.properties.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.SlugField(unique=True, max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(null=True, upload_to=resty.apps.properties.models.image_path_post, blank=True)),
                ('description', models.TextField(max_length=1000, null=True, blank=True)),
                ('latitude', models.CharField(max_length=100)),
                ('longitude', models.CharField(max_length=100)),
                ('price', models.DecimalField(default=0.0, max_digits=10, decimal_places=2)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Casa',
                'verbose_name_plural': 'Casas',
            },
        ),
    ]
