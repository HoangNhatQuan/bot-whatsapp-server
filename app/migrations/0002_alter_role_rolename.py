# Generated by Django 5.1.1 on 2024-09-26 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='roleName',
            field=models.TextField(unique=True),
        ),
    ]
