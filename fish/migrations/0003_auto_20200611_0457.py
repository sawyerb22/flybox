# Generated by Django 2.2.13 on 2020-06-11 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fish', '0002_auto_20200610_2041'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fish',
            old_name='type',
            new_name='species',
        ),
    ]
