# Generated by Django 4.2.3 on 2023-07-08 16:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchhistory',
            name='last_searched',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
