from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


class WriterManager(BaseUserManager):

    '''
        Esta funcion es para crear usuarios y guardarlos en la DB
        Para los demas modelos, esta forma es similar, asi ocurre en background.
    '''

    def create_user(self, email, first_name, last_name, web_site=None, signing=None, password=None):

        if not email:
            raise ValueError("Usuario debe tener un email válido")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            web_site=web_site,
            signing=signing,
        )
        user.set_password(password)
        user.save(using=self._db)  #_db ocupa el default DB, al igual si se omite el parametro, si se ocupa otra DB, sede be espeficiar
        return user

    '''
        Esta funcios solamente temporal para administrar datos en el panel /admin
    '''

    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(email, first_name=first_name, last_name=last_name, password=password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Writer(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    web_site = models.CharField(max_length=255, null=True, blank=True)
    signing = models.CharField(max_length=128, null=True, blank=True)
    writer_level = models.IntegerField(default=1, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, auto_now=False)  # auto_created

    ''' Campos temporales para administrar en panel admin '''
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = WriterManager()

    USERNAME_FIELD = 'email'  # Indica la PK del usuario custom
    REQUIRED_FIELDS = ['first_name', 'last_name']  # Todos los campos blank=False

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"

    def has_perm(self, perm, obj=None):
        '''
            Verifica si tiene cierto permiso
        '''
        return True

    def has_module_perms(self, app_label):
        '''
            Verifica si tiene permiso para cierta acción
        '''
        return True

   # @property
    #def writer_level(self):
     #   return self.writer_level
