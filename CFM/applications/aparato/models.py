from django.db import models
from django.db.models.deletion import CASCADE

"""
Define el modelo relacional "Aparato" en la base de datos.

Hasta el momento el único Aparato disponible es el 
Cabezal 622, pero en versiones futuras será posible
expandir a otros aparatos.
"""
class Aparato(models.Model):
    id_aparato = models.BigAutoField(primary_key=True)
    nombre = models.CharField('Nombre del aparato',max_length=40)

    def __str__(self):
        return str(self.id_aparato) + '. ' + str(self.nombre)