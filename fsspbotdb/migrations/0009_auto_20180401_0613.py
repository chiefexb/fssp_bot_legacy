# Generated by Django 2.0.1 on 2018-04-01 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fsspbotdb', '0008_auto_20180331_2217'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cookie',
            old_name='value_name',
            new_name='valuename',
        ),
    ]