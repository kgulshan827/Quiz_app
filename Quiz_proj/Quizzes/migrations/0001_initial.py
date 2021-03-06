# Generated by Django 3.1.6 on 2021-04-21 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('topic', models.CharField(max_length=100)),
                ('number_of_ques', models.IntegerField()),
                ('time', models.IntegerField()),
                ('required_score', models.IntegerField()),
                ('difficulty', models.CharField(choices=[('easy', 'easy'), ('medium', 'medium'), ('hard', 'hard')], max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Quizes',
            },
        ),
    ]
