# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_manager', '0002_auto_20140929_2028'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestPlan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('test_time', models.FloatField()),
                ('interval', models.PositiveSmallIntegerField()),
                ('started', models.DateTimeField(auto_now_add=True)),
                ('query', models.ForeignKey(to='api_manager.Query')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
