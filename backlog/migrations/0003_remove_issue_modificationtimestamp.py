# Generated by Django 3.0.4 on 2020-05-22 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backlog', '0002_issue_elapsedtime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='modificationTimeStamp',
        ),
    ]