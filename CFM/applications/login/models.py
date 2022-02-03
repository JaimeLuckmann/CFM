#from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager 

#PermissionsMixin sirve para poder crear usuarios desde la consola.
class User(AbstractBaseUser,PermissionsMixin,models.Model):

    #El campo username debe estar en la creación de usuarios.
    username = models.CharField(max_length=20,unique=True)
    email = models.EmailField()
    nombre = models.CharField(max_length=30)
    primerApellido = models.CharField(max_length=15)
    segundoApellido = models.CharField(max_length=15)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    #Los atributos obligatorios a parte de username y password.
    REQUIRED_FIELDS = ['email',]

    objects = UserManager()

    def __str__(self):
        return  self.nombre + ' ' + self.primerApellido


