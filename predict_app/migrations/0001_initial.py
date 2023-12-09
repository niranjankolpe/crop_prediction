# Generated by Django 4.2.3 on 2023-07-29 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CropData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('N', models.IntegerField()),
                ('P', models.IntegerField()),
                ('K', models.IntegerField()),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('ph', models.FloatField()),
                ('rainfall', models.FloatField()),
                ('prediction', models.TextField()),
            ],
        ),
    ]