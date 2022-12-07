# Generated by Django 3.1.4 on 2022-12-07 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='moviebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('movie', models.CharField(choices=[('Sholey', 'Sholey 1975'), ('Avengers', 'Avengers end game'), ('Harry Potter', 'Harry potter and prizoner of Azkaban')], max_length=200)),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
