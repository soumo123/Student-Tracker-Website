# Generated by Django 3.2 on 2021-05-31 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home1', '0003_rename_image_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='images/civil.jpg', upload_to='media/profile_pics'),
        ),
    ]