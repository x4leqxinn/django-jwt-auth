# Generated by Django 4.2.2 on 2023-06-16 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
    ]
