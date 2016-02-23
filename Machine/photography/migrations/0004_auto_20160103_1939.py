# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photography', '0003_auto_20160103_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='dislike_cnt',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='favor_cnt',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
