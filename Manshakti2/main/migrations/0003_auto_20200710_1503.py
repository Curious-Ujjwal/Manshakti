# Generated by Django 3.0.8 on 2020-07-10 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200710_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='admin_approved',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='story',
            name='pub_date',
            field=models.DateTimeField(default='2000-06-03 03:08:50.262391'),
        ),
    ]
