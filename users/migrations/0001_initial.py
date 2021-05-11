# Generated by Django 3.2.2 on 2021-05-09 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserEmail', models.EmailField(max_length=500)),
                ('UserPassword', models.CharField(max_length=500)),
                ('UserFirstName', models.CharField(max_length=50)),
                ('UserLastName', models.CharField(max_length=50)),
                ('UserCity', models.CharField(max_length=90)),
                ('UserState', models.CharField(max_length=20)),
                ('UserZip', models.CharField(max_length=20)),
                ('UserEmailVerified', models.IntegerField(default=1)),
                ('UserRegistrationDate', models.DateTimeField(auto_now=True)),
                ('UserVerificationCode', models.CharField(max_length=20)),
                ('UserIP', models.CharField(max_length=50)),
                ('UserPhone', models.CharField(max_length=20)),
                ('UserFax', models.CharField(max_length=20)),
                ('UserCountry', models.CharField(max_length=20)),
                ('UserAddress', models.CharField(max_length=100)),
                ('UserAddress2', models.CharField(max_length=50)),
            ],
        ),
    ]
