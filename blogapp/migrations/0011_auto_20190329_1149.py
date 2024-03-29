# Generated by Django 2.1.7 on 2019-03-29 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0010_signatures'),
    ]

    operations = [
        migrations.AddField(
            model_name='signatures',
            name='decryptedText_bobRoss',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='signatures',
            name='decryptedText_daVinci',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='signatures',
            name='bobRossPrivKey',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='signatures',
            name='bobRossPubKey',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='signatures',
            name='daVinciPrivKey',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='signatures',
            name='daVinciPubKey',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='signatures',
            name='text',
            field=models.TextField(null=True),
        ),
    ]
