# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signapps', '0002_auto_20150124_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='last_name',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
    ]
