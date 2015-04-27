# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=256, verbose_name='Name')),
                ('last_name', models.CharField(max_length=256, verbose_name='Surname')),
                ('middle_name', models.CharField(default=b'', max_length=256, verbose_name='Middle name', blank=True)),
                ('birthday', models.DateField(null=True, verbose_name='date of Birth')),
                ('photo', models.ImageField(upload_to=b'', null=True, verbose_name='Photo', blank=True)),
                ('ticket', models.CharField(max_length=256, verbose_name='Ticket')),
                ('notes', models.TextField(verbose_name='Remarks', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
