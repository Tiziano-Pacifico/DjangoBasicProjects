# Generated by Django 5.1.2 on 2024-11-08 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='desegnation',
            new_name='designation',
        ),
    ]
