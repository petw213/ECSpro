# Generated by Django 3.0.5 on 2020-04-13 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_post_posturl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postDate',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='postWriter',
            field=models.TextField(null=True),
        ),
    ]
