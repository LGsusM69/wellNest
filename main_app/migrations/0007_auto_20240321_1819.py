# Generated by Django 3.2.12 on 2024-03-21 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_journal_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dailycheckin',
            old_name='dailyPractices',
            new_name='exerciseType',
        ),
        migrations.RenameField(
            model_name='dailycheckin',
            old_name='exercise',
            new_name='intensity',
        ),
        migrations.AddField(
            model_name='dailycheckin',
            name='duration',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='dailycheckin',
            name='improvements',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dailycheckin',
            name='practices',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
