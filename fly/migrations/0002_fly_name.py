# Generated by Django 2.2.10 on 2020-06-10 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fly', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fly',
            name='name',
            field=models.CharField(default='sow bug', max_length=50),
            preserve_default=False,
        ),
    ]