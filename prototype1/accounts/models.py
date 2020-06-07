from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self, username, first_name, last_name, subject, chapter, password):
        values = [username, first_name, last_name, subject, chapter]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError('The {} value must be set'.format(field_name))

        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            subject=subject,
            chapter=chapter
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=254,unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    subject = models.CharField(max_length=100)
    chapter = models.CharField(max_length=100)
    is_permitted = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'subject', 'chapter']

    def __str__(self):
        return '{} '.format(self.first_name)