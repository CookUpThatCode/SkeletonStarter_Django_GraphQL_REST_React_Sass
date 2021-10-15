from django.db import models
from django.contrib.auth import get_user_model 
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db.models.expressions import Value


class CustomAccountManager(BaseUserManager):
    def create_user(self, username, email, password, **otherFields):
        if not username or not email or not password:
            raise ValueError("You must provide all the required fields")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **otherFields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password, **otherFields):
        otherFields.setdefault('is_staff', True)
        otherFields.setdefault('is_superuser', True)
        otherFields.setdefault('is_active', True)

        if otherFields.get('is_staff') is not True or otherFields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_staff and is_superuser equal True')

        return self.create_user(username, email, password, **otherFields)
    
class Hiker(AbstractBaseUser, PermissionsMixin):
    # PermissionsMixin auto includes stuff like isSuperUser
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    firstName = models.CharField(max_length=150, blank=True)
    lastName = models.CharField(max_length=150, blank=True)
    bio = models.TextField(max_length=1000, blank=True)
    accountCreation = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)   # FIX: have False so when sign up, have to authorize account through email.
    is_staff = models.BooleanField(default=False)  

    city = models.CharField(max_length=50, blank=True)
    image = models.ImageField(null=True, blank=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']     # for making a superuser with createsuperuser.

    def __str__(self):
        return self.username

class Trail(models.Model):
    name = models.CharField(max_length=50)

class Hike(models.Model):
    trail = models.ForeignKey('uhg.Trail', related_name='hikes', on_delete=models.CASCADE)
    hiker = models.ForeignKey(get_user_model(), related_name='hikes', on_delete=models.CASCADE)
    checkInDate = models.DateTimeField(auto_now_add=True)