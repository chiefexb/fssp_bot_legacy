# Generated by Django 2.0.1 on 2018-03-31 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fsspbotdb', '0007_telegram_session_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cookie',
            old_name='name',
            new_name='value',
        ),
    ]
