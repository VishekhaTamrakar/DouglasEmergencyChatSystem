# Generated by Django 2.1.7 on 2019-04-03 02:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_auto_20190401_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='invited',
            field=models.ManyToManyField(blank=True, null=True, related_name='invited_user', to=settings.AUTH_USER_MODEL, verbose_name='Participants'),
        ),
    ]
