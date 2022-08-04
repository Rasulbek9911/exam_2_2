# Generated by Django 4.0.6 on 2022-08-02 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_online',
            field=models.CharField(choices=[('online', 'On-line'), ('offline', 'Off-line')], default='offline', max_length=25),
        ),
    ]