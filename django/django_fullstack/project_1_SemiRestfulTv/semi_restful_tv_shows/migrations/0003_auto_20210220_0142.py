# Generated by Django 2.2.4 on 2021-02-20 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('semi_restful_tv_shows', '0002_auto_20210220_0016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='show',
            old_name='name',
            new_name='title',
        ),
    ]
