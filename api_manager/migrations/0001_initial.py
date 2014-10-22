# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import api_manager.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Api',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('base_url', models.CharField(max_length=64, validators=[api_manager.models._validate_base_url])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('method', models.CharField(default=b'GET', max_length=6, choices=[(b'GET', b'GET'), (b'POST', b'POST'), (b'PUT', b'PUT'), (b'DELETE', b'DELETE')])),
                ('url', models.CharField(max_length=64, null=True)),
                ('body', models.TextField(null=True, validators=[api_manager.models._validate_body])),
                ('api', models.ForeignKey(to='api_manager.Api')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
