# Generated by Django 4.2.11 on 2024-03-21 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='journal_photos/'),
        ),
    ]