# Generated by Django 3.0.8 on 2020-08-14 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bed',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='icu',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
