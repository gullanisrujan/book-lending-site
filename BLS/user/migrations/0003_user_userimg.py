# Generated by Django 3.1.5 on 2022-01-22 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_expectedbooks'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='userImg',
            field=models.ImageField(default=None, upload_to='images/'),
            preserve_default=False,
        ),
    ]
