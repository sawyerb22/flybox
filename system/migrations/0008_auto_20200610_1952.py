# Generated by Django 2.2.10 on 2020-06-10 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0007_auto_20200610_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='fish',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fish_image', to='fish.Fish'),
        ),
    ]
