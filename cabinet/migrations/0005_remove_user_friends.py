# Generated by Django 3.0.2 on 2020-05-26 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0004_user_friends'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='friends',
        ),
    ]
