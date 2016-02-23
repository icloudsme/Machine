# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=256, null=True, blank=True)),
                ('photo_link', models.CharField(max_length=128)),
                ('upload_time', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'ordering': ('upload_time',),
                'db_table': 'photo',
                'verbose_name': '\u7167\u7247',
                'verbose_name_plural': '\u7167\u7247',
            },
        ),
    ]
