# Generated by Django 2.1.7 on 2019-06-30 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_auto_20190630_0840'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='img',
            field=models.CharField(default='https://image.flaticon.com/icons/svg/149/149071.svg', max_length=500),
        ),
        migrations.AddField(
            model_name='trustee',
            name='img',
            field=models.CharField(default='https://image.flaticon.com/icons/svg/149/149071.svg', max_length=500),
        ),
    ]
