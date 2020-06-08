from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from ckeditor_uploader.fields import RichTextUploadingField

class UserManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self, username, first_name, last_name, subject, chapter, password, **extra_fields):
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
            chapter=chapter,
            is_superuser=extra_fields['is_superuser'],
            is_staff=extra_fields['is_staff'],
            is_active=extra_fields['is_active'],
            is_permitted=extra_fields['is_permitted'],
            is_admin=extra_fields['is_admin']
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, first_name, last_name, subject, chapter, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(username, first_name, last_name, subject, chapter, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=254,unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    subject = models.CharField(max_length=100)
    chapter = models.CharField(max_length=100)
    is_permitted = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'subject', 'chapter']

    def __str__(self):
        return '{} '.format(self.first_name)

class CK(models.Model):
	content = RichTextUploadingField()

	def __str__(self):
		return self.content