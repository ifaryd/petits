# Generated by Django 3.0 on 2020-06-24 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='activité',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('titre', models.TextField()),
                ('contenue', models.TextField()),
            ],
        ),
    ]
