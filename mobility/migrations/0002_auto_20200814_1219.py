# Generated by Django 3.0.8 on 2020-08-14 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobility', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobility',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='mobility',
            name='visit_rate',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
