# Generated by Django 5.1 on 2024-09-11 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0016_comment_parent_alter_comment_content_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
    ]
