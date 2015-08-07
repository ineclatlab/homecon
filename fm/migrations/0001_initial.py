# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FmChange',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('fmchange_at', models.DateTimeField(auto_now=True)),
                ('packet', models.TextField()),
                ('siliconid', models.CharField(max_length=20)),
            ],
        ),
    ]
