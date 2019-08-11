# Generated by Django 2.1.7 on 2019-08-10 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0007_auto_20190810_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='position',
        ),
        migrations.RemoveField(
            model_name='trustee',
            name='conact_tel',
        ),
        migrations.AddField(
            model_name='member',
            name='phone',
            field=models.CharField(default='0', max_length=11),
        ),
        migrations.AddField(
            model_name='trustee',
            name='email',
            field=models.CharField(default='@', max_length=100),
        ),
        migrations.AddField(
            model_name='trustee',
            name='phone',
            field=models.CharField(default='0', max_length=11),
        ),
        migrations.AlterField(
            model_name='trustee',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
