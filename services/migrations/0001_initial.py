# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pings',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('ping_at', models.DateTimeField(auto_now=True)),
                ('packet', models.TextField()),
                ('siliconid', models.CharField(max_length=20)),
            ],
        ),
    ]
