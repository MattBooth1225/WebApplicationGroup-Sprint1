# Generated by Django 4.1.2 on 2022-12-12 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_cardnum',
            field=models.IntegerField(default=0, max_length=16),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_exp_date',
            field=models.CharField(default='00/00', max_length=5),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_sec_code',
            field=models.IntegerField(default=123, max_length=3),
        ),
    ]
