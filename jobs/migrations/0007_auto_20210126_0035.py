# Generated by Django 2.2.8 on 2021-01-25 20:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_jobpost_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobadmin',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='job_admin_name', to=settings.AUTH_USER_MODEL),
        ),
    ]