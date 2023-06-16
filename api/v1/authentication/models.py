from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserRole(models.Model):
    description = models.CharField(max_length=100,null=False,blank=False,unique=True)

    def __str__(self):
        return self.description
    class Meta:
        db_table = 'user_role'
        verbose_name_plural = 'Roles de usuario'

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('El nombre de usuario debe ser proporcionado')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('user_role_id', 1)
        return self._create_user(username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True,blank=True,null=True)
    username = models.CharField(max_length=30, blank=True, null=True,unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    user_role = models.ForeignKey(UserRole,on_delete=models.CASCADE)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        full_name = '{} {}'.format(self.first_name, self.last_name)
        return full_name.strip()

    class Meta:
        db_table = 'user'
        verbose_name_plural = 'Usuarios'

from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    failed_attempts = models.PositiveIntegerField(default=0)
    locked_until = models.DateTimeField(default=None, null=True, blank=True)

    def __str__(self):
        return self.user.username

    def increment_failed_attempts(self):
        self.failed_attempts += 1
        self.save()

    def reset_failed_attempts(self):
        self.failed_attempts = 0
        self.save()
    
    def lock_account(self, minutes):
        self.locked_until = timezone.now() + timezone.timedelta(minutes=minutes)
        self.save()


    def is_account_locked(self):
        return self.locked_until is not None and self.locked_until > timezone.now()
    
    class Meta:
        db_table = 'user_profile'
        verbose_name_plural = 'Perfiles de usuario'
