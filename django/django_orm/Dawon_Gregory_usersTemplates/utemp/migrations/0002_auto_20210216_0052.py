# Generated by Django 2.2.4 on 2021-02-16 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utemp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
    ]