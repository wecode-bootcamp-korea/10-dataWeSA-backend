# Generated by Django 3.0.8 on 2020-08-06 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('daily', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Icu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('total_per_capita', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField()),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='daily.State')),
            ],
            options={
                'db_table': 'icu',
            },
        ),
        migrations.CreateModel(
            name='Bed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beds_per_thousand', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField()),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='beds', to='daily.State')),
            ],
            options={
                'db_table': 'beds',
            },
        ),
    ]
