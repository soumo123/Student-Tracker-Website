# Generated by Django 3.2 on 2021-05-25 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20210525_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='img',
            field=models.ImageField(default='gmit5.jpg', null=True, upload_to='profile_pics'),
        ),
    ]