# Generated by Django 4.2.1 on 2023-07-17 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profilepic.jpg', upload_to='pictures'),
        ),
    ]