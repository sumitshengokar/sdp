# Generated by Django 2.2.3 on 2020-04-28 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0003_auto_20200428_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweets',
            name='reply',
            field=models.CharField(default=False, max_length=100),
        ),
        migrations.AddField(
            model_name='tweets',
            name='retweeted',
            field=models.CharField(default=False, max_length=100),
        ),
    ]
