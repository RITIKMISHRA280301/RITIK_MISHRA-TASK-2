# Generated by Django 4.0 on 2023-03-27 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drone_booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
