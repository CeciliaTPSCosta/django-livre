# Generated by Django 3.2.9 on 2021-12-03 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_auto_20211203_0413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_number',
            field=models.IntegerField(default=10028, unique=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
