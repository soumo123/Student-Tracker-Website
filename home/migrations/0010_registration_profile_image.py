# Generated by Django 3.2 on 2021-05-22 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_delete_cdc'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]