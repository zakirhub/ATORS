# Generated by Django 4.0.5 on 2022-09-13 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0004_booked_ticket_name_booked_ticket_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=100)),
            ],
        ),
    ]