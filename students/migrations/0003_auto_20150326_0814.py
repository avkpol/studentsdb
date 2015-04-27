# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20150326_0759'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='group_leader',
            new_name='leader',
        ),
    ]
