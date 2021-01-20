# Generated by Django 2.2.8 on 2021-01-17 23:12

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('travelblog', '0002_blog_view_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='content',
            field=tinymce.models.HTMLField(default='test', verbose_name='Content'),
            preserve_default=False,
        ),
    ]
