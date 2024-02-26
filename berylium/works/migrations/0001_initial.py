# Generated by Django 4.2.10 on 2024-02-26 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='slider_works')),
                ('place_of_interest', models.CharField(max_length=200, verbose_name='place of interest')),
                ('location', models.CharField(max_length=200, verbose_name='location')),
            ],
            options={
                'verbose_name': 'images for slider',
                'db_table': 'pictures in work page',
            },
        ),
    ]
