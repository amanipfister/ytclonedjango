# Generated by Django 4.1.7 on 2023-02-22 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ytApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]