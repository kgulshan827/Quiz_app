# Generated by Django 3.1.6 on 2021-05-12 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Answer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='user',
        ),
    ]