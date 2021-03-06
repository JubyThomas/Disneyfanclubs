# Generated by Django 2.1.5 on 2021-08-02 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20210731_0028'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieLists',
            fields=[
                ('movieid', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=120)),
                ('fullTitle', models.CharField(max_length=250)),
                ('yearreleased', models.IntegerField(null=True)),
                ('imgpath', models.CharField(max_length=400)),
                ('imdbrating', models.FloatField(null=True)),
                ('description', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ['-movieid'],
            },
        ),
    ]
