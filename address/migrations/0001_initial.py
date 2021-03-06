# Generated by Django 2.2.5 on 2019-09-25 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('iso_code', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name_plural': 'Countries',
                'ordering': ['name', 'iso_code'],
            },
        ),
        migrations.CreateModel(
            name='StateProvince',
            fields=[
                ('iso_code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=55)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.Country')),
            ],
            options={
                'verbose_name': 'State or province',
                'ordering': ['-country', 'name'],
            },
        ),
    ]
