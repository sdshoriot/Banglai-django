# Generated by Django 2.1.2 on 2018-11-02 13:18

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20181102_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='detail',
            field=tinymce.models.HTMLField(),
        ),
    ]