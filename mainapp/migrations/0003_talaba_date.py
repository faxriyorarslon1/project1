# Generated by Django 3.2.11 on 2022-01-12 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20220112_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='talaba',
            name='date',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mainapp.datetime'),
        ),
    ]
