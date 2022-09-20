# Generated by Django 4.0.5 on 2022-09-11 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_booked_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='booked_ticket',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='booked_ticket',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
