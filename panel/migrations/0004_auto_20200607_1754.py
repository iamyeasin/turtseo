# Generated by Django 3.0.6 on 2020-06-07 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0003_link_counter'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile_extended',
            name='domanin_rank',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='profile_extended',
            name='domanin_auth',
            field=models.CharField(default='', max_length=500),
        ),
    ]
