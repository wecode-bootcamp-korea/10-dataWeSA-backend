# Generated by Django 3.0.8 on 2020-08-14 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('economy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='economicstatus',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='employmentstatus',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]