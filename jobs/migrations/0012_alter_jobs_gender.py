# Generated by Django 3.2.12 on 2022-02-19 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0011_auto_20220219_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='gender',
            field=models.BooleanField(choices=[(None, 'other'), (True, "'male"), (False, 'female')], null=True),
        ),
    ]
