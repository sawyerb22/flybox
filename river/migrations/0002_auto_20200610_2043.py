# Generated by Django 2.2.10 on 2020-06-10 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('river', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hole',
            name='river',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='river_hole', to='river.River'),
        ),
    ]
