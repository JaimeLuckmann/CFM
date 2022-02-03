from django.db import models
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager,models.Manager):

    def _create_user(self,username,email,password,is_staff,is_superuser,**extra_fields):

        user = self.model(
            username = username,
            email = email,
            #Permisos de administrador:
            is_staff = is_staff,
            #Permisos de super usuario:
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)

    #Tipo de usuario con permisos de super usuario.
    def create_superuser(self, username,email,password,**extra_fields):
        return self._create_user(username,email,password,is_staff=False,is_superuser=True,**extra_fields)

    #Tipo de usuario con derechos a administrador (precios, nombres,etc).
    def create_adminuser(self, username,email,password,**extra_fields):
        return self._create_user(username,email,password,is_staff=False,is_superuser=False,is_active=False,**extra_fields)

    #Tipo de usuario sin ningún tipo de permiso
    def create_user(self, username,email,password,**extra_fields):
        return self._create_user(username,email,password,is_staff=False,is_superuser=False,is_active=False**extra_fields)