# Generated by Django 2.1.2 on 2018-11-03 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20181103_0909'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='post_description',
        ),
    ]