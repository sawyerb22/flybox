# Generated by Django 2.2.8 on 2020-01-23 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0007_auto_20200121_0425'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='address',
            unique_together=set(),
        ),
    ]
