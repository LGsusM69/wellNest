# Generated by Django 4.2.4 on 2024-03-22 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_alter_dailycheckin_date_alter_dailycheckin_diet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailycheckin',
            name='sleep',
            field=models.IntegerField(default=50),
        ),
    ]