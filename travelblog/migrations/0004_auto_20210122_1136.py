# Generated by Django 2.2.8 on 2021-01-22 07:36

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelblog', '0003_remove_blog_comment_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='content',
        ),
        migrations.AddField(
            model_name='blog',
            name='richcontent',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
