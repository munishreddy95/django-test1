# Generated by Django 3.0.5 on 2020-05-11 08:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 11, 14, 7, 24, 924066)),
        ),
    ]
