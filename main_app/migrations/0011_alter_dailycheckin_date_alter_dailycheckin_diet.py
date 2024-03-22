# Generated by Django 4.2.4 on 2024-03-22 01:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_merge_20240321_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailycheckin',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='dailycheckin',
            name='diet',
            field=models.TextField(max_length=500),
        ),
    ]
