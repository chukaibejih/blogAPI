# Generated by Django 4.0.3 on 2022-03-17 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='authur',
            new_name='author',
        ),
    ]
