# Generated by Django 4.2.3 on 2023-07-31 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predict_app', '0002_cropdata_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cropdata',
            name='K',
        ),
        migrations.RemoveField(
            model_name='cropdata',
            name='N',
        ),
        migrations.RemoveField(
            model_name='cropdata',
            name='P',
        ),
        migrations.RemoveField(
            model_name='cropdata',
            name='date',
        ),
        migrations.RemoveField(
            model_name='cropdata',
            name='humidity',
        ),
        migrations.RemoveField(
            model_name='cropdata',
            name='ph',
        ),
        migrations.RemoveField(
            model_name='cropdata',
            name='prediction',
        ),
        migrations.RemoveField(
            model_name='cropdata',
            name='rainfall',
        ),
        migrations.RemoveField(
            model_name='cropdata',
            name='temperature',
        ),
    ]
