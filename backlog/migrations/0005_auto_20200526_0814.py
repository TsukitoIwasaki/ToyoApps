# Generated by Django 2.0.4 on 2020-05-26 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backlog', '0004_auto_20200526_0755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='invoicedetail',
            name='invoice',
        ),
        migrations.RemoveField(
            model_name='invoicedetail',
            name='item',
        ),
        migrations.DeleteModel(
            name='Invoice',
        ),
        migrations.DeleteModel(
            name='InvoiceDetail',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
