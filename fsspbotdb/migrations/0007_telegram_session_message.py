# Generated by Django 2.0.1 on 2018-03-31 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fsspbotdb', '0006_telegram_session_chat_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegram_session',
            name='message',
            field=models.CharField(blank='False', max_length=100, null='False'),
        ),
    ]
