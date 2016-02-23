# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photography', '0002_photo_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Remark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=256, null=True, blank=True)),
                ('create_time', models.DateTimeField(null=True, blank=True)),
                ('author', models.ForeignKey(verbose_name='User', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('create_time',),
                'db_table': 'remark',
                'verbose_name': '\u7167\u7247',
                'verbose_name_plural': '\u7167\u7247',
            },
        ),
        migrations.AddField(
            model_name='photo',
            name='dislike_cnt',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='favor_cnt',
            field=models.IntegerField(null=True),
        ),
    ]
