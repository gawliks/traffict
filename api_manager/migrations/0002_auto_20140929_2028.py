# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import api_manager.models


class Migration(migrations.Migration):

    dependencies = [
        ('api_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='body',
            field=models.TextField(blank=True, null=True, validators=[api_manager.models._validate_body]),
        ),
        migrations.AlterField(
            model_name='query',
            name='url',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
    ]
