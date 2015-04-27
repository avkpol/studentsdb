# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_studexam'),
    ]

    operations = [
        migrations.AddField(
            model_name='studexam',
            name='group_exam',
            field=models.CharField(default=b'', max_length=256, verbose_name='\u0413\u0440\u0443\u043f\u0430'),
            preserve_default=True,
        ),
    ]
