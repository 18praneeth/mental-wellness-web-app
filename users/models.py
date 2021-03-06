from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from PIL import Image


# creating custom UserProfile Account Manager
class MyAccountManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have email Id")

        user = self.model(email=self.normalize_email(email), username=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email=self.normalize_email(email),
                                password=password)
        user.role = 'ADM'
        user.username = self.normalize_email(email)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# creating custom user
class User(AbstractUser):
    email = models.EmailField(verbose_name="Email", unique=True)
    ROLE_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    username = models.CharField(max_length=100, unique=False, null=True, blank=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=10, choices=ROLE_CHOICES, null=True)
    name = models.CharField(max_length=30, null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    date_of_birth = models.DateField(null=True)
    phone_number = models.BigIntegerField(null=True)
    college_name = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=200, blank=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyAccountManager()

    def __str__(self):
        if self.name:
            return f'{self.name} - {self.email}'
        else:
            return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        self.username = self.email
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
