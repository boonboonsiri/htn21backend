# Generated by Django 3.1.5 on 2021-01-17 03:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]