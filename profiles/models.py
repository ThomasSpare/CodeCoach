from django.core.management import call_command
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from cloudinary.models import CloudinaryField
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()


class UserManager(BaseUserManager):
    """
    Admin Create and saves a User with the given username, email and password.
    """
    def create_user(
            self,
            username=None,
            email=None,
            password=None,
        ):
            user = self.model(
                username=username,
                email=self.normalize_email(email),
            )
            user.set_password(password)
            user.save(using=self._db)
            user.is_staff = False
            user.save(using=self._db)
            return user

    def create_superuser(self, username, email, password):
        owner = User.objects.create(name='User')
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            owner = owner,
        )

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return self._create_user(username, email, password, owner=owner)


class UserAccount(AbstractUser):
   avatar = CloudinaryField(
       "avatar",
       folder="profile_pics",
       null=True,
       blank=True,
   )
   owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
   email = models.EmailField(default=None, null=True, max_length=254)
   date_joined = models.DateTimeField(unique=True, null=True)
   birth_date = models.DateField(unique=True, null=True)
   first_name = models.CharField(max_length=50)
   last_name = models.CharField(max_length=50)
   country = models.CharField(max_length=100)
   parent = models.BooleanField(default=None, null=True)
   username = models.CharField(unique=True, default=None, null=True, max_length=50)

   objects = UserManager()

   def __str__(self):
       return f"{self.username} {self.first_name} {self.last_name}"

   def age(self):
       today = date.today()
       return (
           today.year
           - self.birth_date.year
           - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
       )