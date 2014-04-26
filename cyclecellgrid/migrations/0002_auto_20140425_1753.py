# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        (b'cyclecellgrid', b'0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name=b'cellgrid',
            name=b'color',
            field=models.CharField(default=111111111, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name=b'cellgrid',
            name=b'value',
            field=models.CharField(default=111111111, max_length=20),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name=b'cellgrid',
            name=b'number',
        ),
    ]
