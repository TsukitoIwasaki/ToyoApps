# Generated by Django 2.0.4 on 2020-05-31 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slack', '0004_slackmember'),
    ]

    operations = [
        migrations.AddField(
            model_name='slackmember',
            name='status',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='slackId'),
        ),
    ]
