# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_studexam_group_exam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studexam',
            name='tutor',
            field=models.CharField(max_length=256, verbose_name='\u041f\u0440\u0456\u0437\u0432\u0438\u0449\u0435 \u0432\u0438\u043a\u043b\u0430\u0434\u0430\u0447\u0430'),
            preserve_default=True,
        ),
    ]
