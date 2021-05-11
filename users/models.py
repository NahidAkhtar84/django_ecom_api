from django.db import models

# Create your models here.

class User(models.Model):
    UserEmail = models.EmailField(max_length=500)
    UserPassword = models.CharField(max_length=500)
    UserFirstName = models.CharField(max_length=50)
    UserLastName = models.CharField(max_length=50)
    UserCity = models.CharField(max_length=90)
    UserState = models.CharField(max_length=20)
    UserZip = models.CharField(max_length=20)
    UserEmailVerified = models.BooleanField(default=1)
    UserRegistrationDate = models.DateTimeField(auto_now=True, auto_now_add=False)
    UserVerificationCode = models.CharField(max_length=20)
    UserIP = models.CharField(max_length=50)
    UserPhone = models.CharField(max_length=20)
    UserFax = models.CharField(max_length=20)
    UserCountry = models.CharField(max_length=20)
    UserAddress = models.CharField(max_length=100)
    UserAddress2 = models.CharField(max_length=50)

    def __str__(self):
        return '{} {}'.format(self.UserFirstName, self.UserLastName)