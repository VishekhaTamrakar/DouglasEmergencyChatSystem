# Generated by Django 2.1.7 on 2019-04-03 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_auto_20190402_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='desc',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
