# Generated by Django 3.0.5 on 2020-04-20 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20200413_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='postSubject',
            field=models.TextField(null=True),
        ),
    ]
