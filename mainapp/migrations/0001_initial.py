# Generated by Django 3.2.11 on 2022-01-10 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Talaba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='ismi')),
                ('surname', models.CharField(max_length=15, verbose_name='familya')),
            ],
        ),
    ]
