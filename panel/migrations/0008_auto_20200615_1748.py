# Generated by Django 3.0.6 on 2020-06-15 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0007_auto_20200613_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile_extended',
            name='existing_cost',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='profile_extended',
            name='new_cost',
            field=models.CharField(max_length=50),
        ),
    ]