# Generated by Django 2.2.28 on 2022-12-05 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_load_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aerfg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xcvg', models.BigIntegerField()),
            ],
        ),
    ]
