# Generated by Django 2.2.8 on 2022-03-20 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0022_auto_20220319_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='gender',
            field=models.BooleanField(blank=True, choices=[(None, 'Any'), (True, 'male'), (False, 'female')], null=True),
        ),
    ]
