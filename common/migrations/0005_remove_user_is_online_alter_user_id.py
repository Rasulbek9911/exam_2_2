# Generated by Django 4.0.6 on 2022-08-03 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_merge_0002_user_is_online_0003_user_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_online',
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
