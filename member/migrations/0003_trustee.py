# Generated by Django 2.1.7 on 2019-06-30 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_remove_member_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trustee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forename', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
            ],
        ),
    ]
