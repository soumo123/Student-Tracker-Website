# Generated by Django 3.2 on 2021-05-23 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_registration_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
