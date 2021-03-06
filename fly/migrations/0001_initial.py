# Generated by Django 2.2.10 on 2020-06-10 19:54

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Nymph', 'Nymph'), ('Emerger', 'Emerger'), ('Dry', 'Dry'), ('Streamer', 'Streamer'), ('Wet', 'Wet')], default='Nymph', max_length=10)),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to='user_photos')),
                ('description', models.CharField(max_length=350)),
                ('time_of_year', models.DateField()),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
