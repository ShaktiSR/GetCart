# Generated by Django 3.1.7 on 2021-07-11 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20210710_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='loguser',
            field=models.CharField(default='admin', max_length=30),
        ),
    ]
