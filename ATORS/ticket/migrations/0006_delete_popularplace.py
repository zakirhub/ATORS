# Generated by Django 4.0.5 on 2022-09-13 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0005_message'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PopularPlace',
        ),
    ]