# Generated by Django 2.1.2 on 2018-11-07 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_post_previous_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='previous_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=None, related_name='previous', to='blog.Post'),
        ),
    ]