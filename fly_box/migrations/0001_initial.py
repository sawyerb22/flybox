# Generated by Django 2.2.10 on 2020-06-10 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fly', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlyBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('fly', models.ManyToManyField(related_name='fly', to='fly.Fly')),
            ],
        ),
    ]
