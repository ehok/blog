# Generated by Django 2.1.7 on 2019-03-01 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='key',
            field=models.TextField(default='some strings'),
        ),
    ]
