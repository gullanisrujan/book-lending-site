# Generated by Django 3.1.5 on 2022-01-28 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='transactionId',
            field=models.CharField(max_length=1000),
        ),
    ]
