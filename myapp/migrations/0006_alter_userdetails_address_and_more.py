# Generated by Django 4.2.10 on 2024-02-16 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_userdetails_first_name_userdetails_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='phone_number',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
