# Generated by Django 4.1.3 on 2023-01-09 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplo_dos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Precio',
            field=models.IntegerField(),
        ),
    ]
