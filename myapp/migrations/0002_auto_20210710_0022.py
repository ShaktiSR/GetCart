# Generated by Django 3.1.7 on 2021-07-09 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='option_four_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='poll',
            name='option_one_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='poll',
            name='option_three_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='poll',
            name='option_two_count',
            field=models.IntegerField(default=0),
        ),
    ]
