# Generated by Django 3.2 on 2021-05-30 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='verified',
            field=models.CharField(max_length=122, null=True),
        ),
    ]
