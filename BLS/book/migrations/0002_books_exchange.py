# Generated by Django 3.1.5 on 2022-01-17 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='exchange',
            field=models.BooleanField(default=True),
        ),
    ]
