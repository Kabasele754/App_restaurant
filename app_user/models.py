from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email,user_type, password=None, password2=None, **extra_fields):
        if not email:
            raise ValueError("Email can not be null")
        email = self.normalize_email(email)
        user = self.model(
            email = email,
            user_type = user_type,
            **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email =email,
            user_type= 1,
            password = password
        )
        user.is_admin = True
        user.save(using=self.db)
        return user

# definir user class
class User(AbstractBaseUser):
    GENDER = [("M","Male"),("F","Female")]
    USER_TYPE = ( (1, "Admin"), (2,"Vendor"), (3,"Client") )
    email = models.EmailField(max_length=100, unique=True)
    fistname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER)
    phone = models.CharField(max_length=15, unique=True)
    profile_image = models.ImageField(upload_to="profile/", default="profile/user.png")
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    user_type = models.CharField(max_length=6,default=1, choices=USER_TYPE)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    object = UserManager()
    USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = ["email",]


    @property
    def is_staff(self):
        return self.is_admin


class Employer(models.Model):
    admin = models.OneToOneField(User,on_delete=models.CASCADE)

class Vendor(Employer):
    def __str__(self):
        return f"{self.admin.email}"

class AdminEmployer(Employer):
    def __str__(self):
        return f"{self.admin.email}"


class Client(models.Model):
    admin = models.OneToOneField(User, on_delete=models.CASCADE)
