# Generated by Django 2.0.4 on 2020-06-05 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slack', '0010_slackmember_update_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.TextField(blank=True, max_length=5000, null=True, verbose_name='summary')),
                ('location', models.CharField(blank=True, max_length=255, null=True, verbose_name='location')),
                ('startDate', models.CharField(blank=True, max_length=255, null=True, verbose_name='startDate')),
                ('endDate', models.CharField(blank=True, max_length=255, null=True, verbose_name='endDate')),
                ('iCalUID', models.TextField(blank=True, max_length=5000, null=True, verbose_name='iCalUID')),
                ('etag', models.CharField(blank=True, max_length=255, null=True, verbose_name='etag')),
                ('googleEventId', models.CharField(blank=True, max_length=255, null=True, verbose_name='etag')),
            ],
        ),
    ]