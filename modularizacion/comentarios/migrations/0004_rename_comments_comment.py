# Generated by Django 4.1.4 on 2023-01-06 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0003_comments_signature'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='comments',
            new_name='Comment',
        ),
    ]
