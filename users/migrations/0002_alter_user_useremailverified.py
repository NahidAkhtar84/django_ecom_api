# Generated by Django 3.2.2 on 2021-05-09 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='UserEmailVerified',
            field=models.BooleanField(default=1),
        ),
    ]
