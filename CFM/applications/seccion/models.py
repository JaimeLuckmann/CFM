from django.db import models
from applications.aparato.models import Aparato


"""
Define el modelo relacional Seccion en la base de datos.

Tiene una relación muchos a muchos con el modelo Aparato.

Hasta el momento solamente existe un aparato, el Cabezal 622.
Algunos ejemplos de secciones son: Cuchillo izquierdo, Rodillo
Lateral, Cuchillo flotante, etc.
"""
class Seccion(models.Model):
    id_seccion = models.BigAutoField(primary_key=True)
    nombre = models.CharField('Nombre de la sección',max_length=40)

    aparato = models.ManyToManyField(Aparato)

    def __str__(self):
        return str(self.id_seccion) + '. ' + str(self.nombre)