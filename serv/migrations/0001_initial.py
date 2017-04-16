# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='police',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(default=b'192.168.43.263', max_length=100, null=True, blank=True)),
                ('passwd', models.CharField(default=b'raspberry', max_length=100, null=True, blank=True)),
                ('add', models.CharField(default=b'192.168.43.236', max_length=20)),
                ('money', models.IntegerField(default=0)),
            ],
        ),
    ]
