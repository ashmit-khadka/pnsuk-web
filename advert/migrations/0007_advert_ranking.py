# Generated by Django 2.1.7 on 2019-10-19 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0006_auto_20190927_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='ranking',
            field=models.IntegerField(default=0),
        ),
    ]
