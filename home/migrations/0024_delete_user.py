# Generated by Django 3.2 on 2021-05-31 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_registration_verified'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user',
        ),
    ]
