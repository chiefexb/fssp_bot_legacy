# Generated by Django 2.0.1 on 2018-05-11 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fsspbotdb', '0010_auto_20180507_2107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='chat_id',
        ),
        migrations.AddField(
            model_name='job',
            name='end_date',
            field=models.DateTimeField(auto_now=True, null='True'),
        ),
    ]
